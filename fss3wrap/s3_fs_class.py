from fss3wrap.abstract_fs_class import AbstractFSClass

from fs import open_fs
from fs.base import FS
from fs.copy import copy_file
import boto3

import ntpath

class S3FsClass(AbstractFSClass):

    os_fs = None
    s3_fs = None
    bucket = None
    def __init__(self, s3_parameters, bucket=None, rootdir=None):
        self.reinit(s3_parameters, bucket, rootdir)

    def bytes_write(self, destination_path, destination_file, mbytes):
        self.s3_fs.makedirs(destination_path, recreate=True)
        self.s3_fs.writebytes(
            '{}/{}'.format(destination_path, destination_file), mbytes)

    def directory_list(self, path):
        return self.s3_fs.listdir(path)

    def directory_list_v2(self, path, filter):
        session = boto3.Session(aws_access_key_id=self.s3_parameters['access_key_id'],
                                aws_secret_access_key=self.s3_parameters['secret_access_key'])
        s3_obj = session.client('s3')
        # Return max 1000keys
        prefix, suffix = filter.split('*')[0], filter.split('*')[1]
        kwargs = {'Bucket': self.bucket, 'StartAfter': path, 'Prefix': path+prefix}
        resp = s3_obj.list_objects_v2(**kwargs)
        paths = [elem['Key'] for elem in resp['Contents'] if elem['Key'].endswith(suffix)]
        return paths

    def download(self, source_path, dest_path, filename, mode):
        if mode == 'b':
            file_content = self.file_read_bin(source_path, filename)
        else:
            file_content = self.file_read(source_path, filename)
        path = dest_path + '/' + filename
        f = open(path, 'w+{}'.format(mode))
        f.write(file_content)
        f.close()

    def file_copy(self, source_path, source_file,
                  destination_path, destination_file):
        self.s3_fs.makedirs(destination_path, recreate=True)
        with open('{}/{}'.format(source_path, source_file), 'rb') as read_file:
            # copy LOCAL/bbb to s3://bbb
            self.s3_fs.upload('{}/{}'.format(destination_path,
                                             destination_file), read_file)

    def file_descriptor_copy(self, source_file_descriptor,
                             destination_path, destination_file):
        self.s3_fs.upload('{}/{}'.format(destination_path,
                                         destination_file), source_file_descriptor)

    def file_fd(self, file_path, file_name):
        return self.s3_fs.open('{}/{}'.format(file_path, file_name))

    def file_fd_bin(self, file_path, file_name):
        return self.s3_fs.openbin('{}/{}'.format(file_path, file_name))

    def file_md5(self, file_path, file_name):
        info = self.s3_fs.getinfo(
            '{}/{}'.format(file_path, file_name), namespaces=['s3'])
        return info.raw['s3']['e_tag'][1:-1]

    def file_read(self, source_path, source_file):
        # copy s3://bbb to LOCAL/ccc
        #        priv_os_fs = open_fs('osfs://{}'.format(destination_path))
        #        copy_file(
        #            self.s3_fs,
        #            '{}/{}'.format(source_path, source_file),
        #            priv_os_fs,
        #            destination_file
        #        )
        #
        #        with self.os_fs.open(destination_file) as local_file:
        #            return local_file.read()
        with self.s3_fs.open('{}/{}'.format(source_path, source_file)) as local_file:
            return local_file.read()

    def file_read_bin(self, source_path, source_file):
        with self.s3_fs.openbin('{}/{}'.format(source_path, source_file)) as local_file:
            return local_file.read()

    def file_remove(self, file_path, file_name):
        self.s3_fs.remove('{}/{}'.format(file_path, file_name))

    def reinit(self, s3_parameters, bucket=None, rootdir=None):
        self.os_fs = open_fs('osfs://')
        self.s3_fs = open_fs(
            's3://{}:{}@{}'.format(
                s3_parameters['access_key_id'],
                s3_parameters['secret_access_key'],
                bucket if bucket is not None else s3_parameters['bucket']
            )
        )
        self.s3_parameters = s3_parameters
        self.bucket = bucket if bucket is not None else s3_parameters['bucket']



