from abc import ABC, abstractmethod


class AbstractFSClass(ABC):
    @abstractmethod
    def bytes_write(self, destination_path, destination_file, mbytes):
        pass

    @abstractmethod
    def directory_list(self, path):
        pass

    @abstractmethod
    def directory_list_v2(self, path, filter):
        pass

    @abstractmethod
    def download(self, source_path, dest_path, filename, mode):
        pass

    @abstractmethod
    def file_copy(self, source_path, source_file,
                  destination_path, destination_file):
        pass

    @abstractmethod
    def file_descriptor_copy(self, source_file_descriptor,
                             destination_path, destination_file):
        pass

    @abstractmethod
    def file_fd(self, file_path, file_name):
        pass

    @abstractmethod
    def file_fd_bin(self, file_path, file_name):
        pass

    @abstractmethod
    def file_md5(self, file_path, file_name):
        pass

    @abstractmethod
    def file_read(self, source_path, source_file):
        pass

    @abstractmethod
    def file_read_bin(self, source_path, source_file):
        pass

    @abstractmethod
    def file_remove(self, file_path, file_name):
        pass

    @abstractmethod
    def reinit(self, s3, s3_parameters, bucket, rootdir):
        pass
