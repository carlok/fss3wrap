from fss3wrap.os_fs_class import OsFsClass
from fss3wrap.s3_fs_class import S3FsClass


class Afs():

    afs = None
    s3 = False


    def __init__(self, s3, s3_parameters, bucket=None, rootdir=None):
        self.reinit(s3, s3_parameters, bucket, rootdir)

    def bytes_write(self, destination_path, destination_file, mbytes):
        self.afs.bytes_write(destination_path, destination_file, mbytes)

    def directory_list(self, path):
        return self.afs.directory_list(path)

    def directory_list_v2(self, path, filter):
        return self.afs.directory_list_v2(path, filter)

    def download(self, source_path, dest_path, filename, mode):
        return self.afs.download(source_path, dest_path, filename, mode)

    def file_copy(self, source_path, source_file,
                  destination_path, destination_file):
        self.afs.file_copy(
            source_path,
            source_file,
            destination_path,
            destination_file)

    def file_descriptor_copy(self, source_file_descriptor,
                             destination_path, destination_file):
        self.afs.file_descriptor_copy(
            source_file_descriptor,
            destination_path,
            destination_file)

    def file_fd(self, file_path, file_name):
        return self.afs.file_fd(file_path, file_name)

    def file_fd_bin(self, file_path, file_name):
        return self.afs.file_fd_bin(file_path, file_name)

    def file_md5(self, file_path, file_name):
        return self.afs.file_md5(file_path, file_name)

    def file_read(self, source_path, source_file):
        return self.afs.file_read(source_path, source_file)

    def file_read_bin(self, source_path, source_file):
        return self.afs.file_read_bin(source_path, source_file)

    def file_remove(self, file_path, file_name):
        self.afs.file_remove(file_path, file_name)

    def reinit(self, s3, s3_parameters, bucket=None, rootdir=None):
        if s3 is True:
            self.afs = S3FsClass(s3_parameters, bucket, rootdir)
            self.s3 = True
        else:
            self.afs = OsFsClass(bucket, rootdir)
