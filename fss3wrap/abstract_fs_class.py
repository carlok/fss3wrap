from abc import ABC, abstractmethod
 
class AbstractFSClass(ABC):
    s3_parameters = {
        'access_key_id': '',
        'secret_access_key': '',
        'region': '',
        'bucket': ''
    }
  
    def __init__(self, s3_parameters): 
        self.s3_parameters = s3_parameters

    @abstractmethod
    def bytes_write(self, mfile, mbytes):
        pass

    @abstractmethod
    def directory_list(self, path):
        pass

    @abstractmethod
    def file_copy(self, source_path, source_file, destination_path, destination_file):
        pass

    @abstractmethod
    def file_descriptor_copy(self, source_file_descriptor, destination_path, destination_file):
        pass

    @abstractmethod
    def file_remove(self, file_path, file_name):
        pass

    @abstractmethod
    def file_md5(self, file_path, file_name):
        pass

    @abstractmethod
    def file_read(self, source_path, source_file, destination_path, destination_file):
        pass