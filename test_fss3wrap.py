import os
from dotenv import load_dotenv

from fss3wrap.afs_interface import Afs

import pytest


load_dotenv(override=True)

pytest.aws_bucket_1 = os.getenv('AWS_BUCKET_1')
pytest.aws_bucket_2 = os.getenv('AWS_BUCKET_2')

pytest.fs_path_local = os.getenv('FS_PATH_LOCAL')
pytest.fs_path_remote = os.getenv('FS_PATH_REMOTE')

pytest.s3_parameters = {
    'access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
    'secret_access_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
    'bucket': pytest.aws_bucket_1
}

s3_used = (os.getenv('AWS_S3_USED') == 'True')

pytest.afs = Afs(s3_used, pytest.s3_parameters, pytest.aws_bucket_1, pytest.fs_path_remote)

"""
def test_bytes_write():
    try:
        destination_path = 'extra_sub_folder'
        destination_file = 'destination_file'
        mbytes = b"some initial binary data: \x00\x01"

        pytest.afs.bytes_write(destination_path, destination_file, mbytes)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_directory_list():
    try:
        destination_path = 'extra_sub_folder'

        print(pytest.afs.directory_list(destination_path))
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_copy():
    try:
        source_path = pytest.fs_path_local
        source_file = 'LICENSE'
        destination_path = 'extra_sub_folder'
        destination_file = 'out_LICENSE'

        pytest.afs.file_copy(
            source_path,
            source_file,
            destination_path,
            destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_descriptor_copy():
    try:
        source_path = pytest.fs_path_local
        source_file = 'LICENSE'
        destination_path = 'extra_sub_folder'
        destination_file = 'out_LICENSE'

        with open("{}/{}".format(source_path, source_file), "r") as fd:
            pytest.afs.file_descriptor_copy(fd, destination_path, destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_fd_text():
    try:
        destination_path = 'extra_sub_folder'
        destination_file = 'out_LICENSE'

        print(
            pytest.afs.file_fd(
                destination_path,
                destination_file).read())
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))
"""

# [x] FS [x] S3 : test_bytes_write
# [x] FS [x] S3 : test_directory_list
# [x] FS_BIN [x] FS_TXT [x] S3_BIN [x] S3_TXT : test_file_copy
# [x] FS_BIN [x] FS_TXT [x] S3_BIN [x] S3_TXT : test_file_descriptor_copy
# [x] FS_TXT [x] S3_TXT : test_file_fd_text
# test_file_fd_binary: TODO
# 


def test_file_fd_custom_bucket():
    try:
        custom_bucket = os.getenv('AWS_BUCKET_2')
        source_path = os.getenv('FS_PATH_REMOTE')
        source_file = 'out2_LICENSE'
        afs = Afs(s3_used, s3_parameters, bucket=custom_bucket)

        print(
            afs.file_fd(
                source_path,
                source_file).read())
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


"""
def test_file_md5():
    try:
        file_path = 'extra_sub_folder'
        file_name = 'out_LICENSE'

        print(afs.file_md5(file_path, file_name))
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_read():
    try:
        source_path = os.getenv('FS_PATH_REMOTE')
        source_file = 'out2_LICENSE'
        destination_path = os.getenv('FS_PATH_LOCAL')
        destination_file = 'LICENSE_from_remote'

        print(
            afs.file_read(
                source_path,
                source_file,
                destination_path,
                destination_file))
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_remove():
    try:
        file_path = 'extra_sub_folder'
        file_name = 'out_LICENSE'

        pytest.afs.file_remove(file_path, file_name)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_reinit():
    try:
        s3_parameters = {
            'access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
            'secret_access_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
            'bucket': os.getenv('AWS_BUCKET_2')
        }
        afs.reinit(s3_used, s3_parameters)

        source_path = os.getenv('FS_PATH_LOCAL')
        source_file = 'LICENSE'
        destination_path = os.getenv('FS_PATH_REMOTE')
        destination_file = 'out_LICENSE'

        afs.file_copy(
            source_path,
            source_file,
            destination_path,
            destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))
"""