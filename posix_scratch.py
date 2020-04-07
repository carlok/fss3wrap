import os

from dotenv import load_dotenv

load_dotenv(override=True)

from fs import open_fs
from fs.base import FS
from fs.copy import copy_file
from fs.osfs import OSFS

os_fs = open_fs('osfs://.')

#
# write
#
copy_file(os_fs, '{}bbb'.format(os.getenv('FS_PATH_REMOTE')), os.getenv('FS_PATH_LOCAL'), 'ccc')
os_fs.writebytes('{}mbytes'.format(os.getenv('FS_PATH_REMOTE')), b"some initial binary data: \x00\x01")

#
# read
#
#copy_file(os_fs, 'bbb', './', 'ccc')
with os_fs.open('{}bbb'.format(os.getenv('FS_PATH_LOCAL'))) as local_file:
    print(local_file.read()) # future: return

#
# md5
#
print(os_fs.hash('{}bbb'.format(os.getenv('FS_PATH_LOCAL')), 'md5'))