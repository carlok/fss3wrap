from fss3wrap.abstract_fs_class import AbstractFSClass

from fs import open_fs
from fs.base import FS
from fs.copy import copy_file


import ntpath
import os
import pathlib
import shutil
import glob


class OsFsClass(AbstractFSClass):

    fs_root = None
    os_fs = None

    def __init__(self, bucket=None, rootdir=None):
        self.reinit(bucket, rootdir)

    def bytes_write(self, destination_path, destination_file, mbytes):
        self.os_fs.makedirs(destination_path, recreate=True)
        self.os_fs.writebytes(
            '{}/{}'.format(destination_path, destination_file), mbytes)

    def directory_list(self, path):
        return self.os_fs.listdir(path)

    def directory_list_v2(self, path, filter):
        os_fs = self.fs_root.replace('osfs://', '')
        target = os.path.join(os_fs, path, filter)
        paths = [path for path in glob.glob(target)]
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
        os_fs_destination = open_fs(self.fs_root)
        os_fs_source = open_fs('osfs://' + source_path)

        os_fs_destination.makedirs(destination_path, recreate=True)
        copy_file(
            os_fs_source,
            source_file,
            os_fs_destination,
            destination_path + '/' + destination_file
        )

    def file_descriptor_copy(self, source_file_descriptor,
                             destination_path, destination_file):
        self.os_fs.makedirs(destination_path, recreate=True)

        destination_base_root = self.fs_root[7:]

        f = open('{}/{}'.format(destination_base_root + '/' +
                                destination_path, destination_file), 'wb')
        f.write(source_file_descriptor.read())

    def file_fd(self, file_path, file_name):
        priv_os_fs = open_fs(self.fs_root + file_path)
        return priv_os_fs.open(file_name)

    def file_fd_bin(self, file_path, file_name):
        priv_os_fs = open_fs(self.fs_root + file_path)
        return priv_os_fs.openbin(file_name)

    def file_md5(self, file_path, file_name):
        priv_os_fs = open_fs(self.fs_root + file_path)
        return priv_os_fs.hash(file_name, 'md5')

    def file_read(self, source_path, source_file):
        priv_os_fs = open_fs(self.fs_root + source_path)
        with priv_os_fs.open(source_file) as local_file:
            return local_file.read()

    def file_read_bin(self, source_path, source_file):
        priv_os_fs = open_fs(self.fs_root + source_path)
        with priv_os_fs.openbin(source_file) as local_file:
            return local_file.read()

    def file_remove(self, file_path, file_name):
        self.os_fs.remove('{}/{}'.format(file_path, file_name))

    def reinit(self, bucket=None, rootdir=None):
        self.fs_root = 'osfs://'
        root_path_full = ''

        if rootdir is not None and bucket is not None:
            self.os_fs = open_fs(self.fs_root)
            pathlib.Path('/' + rootdir + '/' + bucket + '/').mkdir(parents=True, exist_ok=True)
            self.fs_root = self.fs_root + rootdir + '/'
            self.fs_root = self.fs_root + bucket + '/'
        else:
            if rootdir is not None:
                root_path_full = rootdir + '/'
                self.os_fs = open_fs(self.fs_root)
                pathlib.Path(root_path_full).mkdir(parents=True, exist_ok=True)
                self.fs_root = self.fs_root + root_path_full + '/'

            if bucket is not None:
                bucket_path_full = bucket + '/'
                self.os_fs = open_fs(self.fs_root)
                pathlib.Path(bucket_path_full).mkdir(parents=True, exist_ok=True)
                self.fs_root = self.fs_root + bucket_path_full + '/'

        self.os_fs = open_fs(self.fs_root)
