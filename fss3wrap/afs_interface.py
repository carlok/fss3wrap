from fss3wrap.os_fs_class import OsFsClass
from fss3wrap.s3_fs_class import S3FsClass

class Afs():

    afs = None
    s3_parameters = None

    def __init__(self, s3_parameters = None):
        if s3_parameters is not None:
            self.afs = S3FsClass(s3_parameters)
            self.s3_parameters = s3_parameters
        else:
            self.afs = OsFsClass()

    def bytes_write(self, mfile, mbytes):
        self.afs.bytes_write(mfile, mbytes)

    def directory_list(self, path):
        return self.afs.directory_list(path)

    def file_copy(self, source_path, source_file, destination_path, destination_file):
        self.afs.file_copy(source_path, source_file, destination_path, destination_file)

    def file_descriptor_copy(self, source_file_descriptor, destination_path, destination_file):
        self.afs.file_descriptor_copy(source_file_descriptor, destination_path, destination_file)

    def file_remove(self, file_path, file_name):
        self.afs.file_remove(file_path, file_name)

    def file_md5(self, file_path, file_name):
        return self.afs.file_md5(file_path, file_name)

    def file_read(self, source_path, source_file, destination_path = None, destination_file = None):
        if self.s3_parameters is not None:
            return self.afs.file_read(source_path, source_file, destination_path, destination_file)
        else:
            return self.afs.file_read(source_path, source_file)
