import os

from dotenv import load_dotenv

from s3_fs_class import S3FsClass

load_dotenv(override=True)

s3_parameters = {
    'access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
    'secret_access_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
    'bucket': os.getenv('AWS_BUCKET')
}

s3_fs = S3FsClass(s3_parameters)

# s3_fs.bytes_write('ccc1', b"some initial binary data: \x00\x01")
# s3_fs.file_copy('./', './', 'README.md', 'README.md')
# s3_fs.file_remove('.', 'bbb')
# print(s3_fs.directory_list('./'))
# print(s3_fs.file_md5('.', 'README.md'))
# print(s3_fs.file_read('.', 'README.md', '.', 'README.md'))