from fss3wrap.abstract_fs_class import AbstractFSClass

from fs import open_fs
from fs.base import FS
from fs.copy import copy_file

import ntpath


class S3FsClass(AbstractFSClass):

    os_fs = None
    s3_fs = None

    def __init__(self, s3_parameters):
        self.os_fs = open_fs('osfs://.')
        self.s3_fs = open_fs(
            's3://{}:{}@{}'.format(
                s3_parameters['access_key_id'],
                s3_parameters['secret_access_key'],
                s3_parameters['bucket']
            )
        )

    def bytes_write(self, destination_path, destination_file, mbytes):
        self.s3_fs.makedirs(destination_path, recreate=True)
        self.s3_fs.writebytes(
            '{}/{}'.format(destination_path, destination_file), mbytes)

    def directory_list(self, path):
        return self.s3_fs.listdir(path)

    def file_copy(self, source_path, source_file,
                  destination_path, destination_file):
        self.s3_fs.makedirs(destination_path, recreate=True)
        with open('{}/{}'.format(source_path, source_file), 'rb') as read_file:
            # copy LOCAL/bbb to s3://bbb
            self.s3_fs.upload('{}/{}'.format(destination_path,
                                             destination_file), read_file)

    def file_descriptor_copy(self, source_file_descriptor,
                             destination_path, destination_file):
        source_path, source_file = ntpath.split(source_file_descriptor.name)
        self.file_copy(
            source_path,
            source_file,
            destination_path,
            destination_file)

    def file_remove(self, file_path, file_name):
        self.s3_fs.remove('{}/{}'.format(file_path, file_name))

    def file_md5(self, file_path, file_name):
        info = self.s3_fs.getinfo(
            '{}/{}'.format(file_path, file_name), namespaces=['s3'])
        return info.raw['s3']['e_tag'][1:-1]

    def file_read(self, source_path, source_file,
                  destination_path, destination_file):
         # copy s3://bbb to LOCAL/ccc
        copy_file(
            self.s3_fs,
            '{}/{}'.format(source_path, source_file),
            self.os_fs,
            '{}/{}'.format(destination_path, destination_file)
        )

        os_fs = open_fs('osfs://.')
        with os_fs.open('{}/{}'.format(destination_path, destination_file)) as local_file:
            return local_file.read()
