# py.test --color=yes -s -v

import os
from dotenv import load_dotenv

from fss3wrap.afs_interface import Afs

import pytest

load_dotenv(override=True)
afs = Afs()

def test_bytes_write():
    try:
        destination_path = os.getenv('FS_PATH_REMOTE')
        destination_file = 'out_LICENSE'
        mbytes = b"some initial binary data: \x00\x01"

        afs.bytes_write(destination_path, destination_file, mbytes)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))

def test_directory_list():
    try:
        print(afs.directory_list(os.getenv('FS_PATH_REMOTE')))
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))

def test_filecopy():
    try:
        source_path = os.getenv('FS_PATH_LOCAL')
        source_file = 'LICENSE'
        destination_path = os.getenv('FS_PATH_REMOTE')
        destination_file = 'out_LICENSE'

        afs.file_copy(source_path, source_file, destination_path, destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))

def test_file_descriptor_copy():
    try:
        source_path = os.getenv('FS_PATH_LOCAL')
        source_file = 'LICENSE'
        destination_path = os.getenv('FS_PATH_REMOTE')
        destination_file = 'out_LICENSE'

        with open("{}/{}".format(source_path, source_file), "r") as fd:
           afs.file_descriptor_copy(fd, destination_path, destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))

def test_file_remove():
    try:
        file_path = os.getenv('FS_PATH_REMOTE')
        file_name = 'out_LICENSE'

        afs.file_remove(file_path, file_name)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))

def test_file_md5():
    try:
        file_path = os.getenv('FS_PATH_REMOTE')
        file_name = 'out2_LICENSE'

        print(afs.file_md5(file_path, file_name))
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))

def test_file_read():
    try:
        source_path = os.getenv('FS_PATH_REMOTE')
        source_file = 'out2_LICENSE'

        print(afs.file_read(source_path, source_file))
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))
