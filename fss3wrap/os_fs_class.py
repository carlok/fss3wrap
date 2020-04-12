from fss3wrap.abstract_fs_class import AbstractFSClass

from fs import open_fs
from fs.base import FS
from fs.copy import copy_file

import ntpath
import shutil


class OsFsClass(AbstractFSClass):

    os_fs = None

    def __init__(self, s3_parameters=None):
        self.os_fs = open_fs('osfs://.')

    def bytes_write(self, destination_path, destination_file, mbytes):
        self.os_fs.makedirs(destination_path, recreate=True)
        self.os_fs.writebytes(
            '{}/{}'.format(destination_path, destination_file), mbytes)

    def directory_list(self, path):
        return self.os_fs.listdir(path)

    def file_copy(self, source_path, source_file,
                  destination_path, destination_file):
        self.os_fs.makedirs(destination_path, recreate=True)
        copy_file(
            self.os_fs,
            '{}/{}'.format(source_path, source_file),
            self.os_fs,
            '{}/{}'.format(destination_path, destination_file)
        )

    def file_descriptor_copy(self, source_file_descriptor,
                             destination_path, destination_file):
        source_path, source_file = ntpath.split(source_file_descriptor.name)
        self.os_fs.makedirs(destination_path, recreate=True)
        shutil.copyfile('{}/{}'.format(source_path, source_file),
                        '{}/{}'.format(destination_path, destination_file))

    def file_remove(self, file_path, file_name):
        self.os_fs.remove('{}/{}'.format(file_path, file_name))

    def file_md5(self, file_path, file_name):
        return self.os_fs.hash('{}/{}'.format(file_path, file_name), 'md5')

    def file_read(self, source_path, source_file,
                  destination_path=None, destination_file=None):
        with self.os_fs.open('{}/{}'.format(source_path, source_file)) as local_file:
            return local_file.read()
