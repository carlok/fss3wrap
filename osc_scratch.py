import os

from dotenv import load_dotenv

from os_fs_class import OsFsClass

load_dotenv(override=True)

os_fs = OsFsClass()

# os_fs.bytes_write('ccc_os', b"some initial binary data: \x00\x01")
os_fs.file_copy('./local', './remote/1/2', 'bbb', 'ccc_dest2')
# os_fs.file_remove('./local', 'bbb')
# print(os_fs.directory_list('./'))
# print(os_fs.file_md5('.', 'README.md'))
# print(os_fs.file_read('.', 'README.md'))