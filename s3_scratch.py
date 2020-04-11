# Costruttore passi sempre
#   dati aws, dati fs (remote path) e flag quale usare (val da env) così interf comune
# Dentro la classe, su flag istanza, un obi o un altro delle _2 classi nascoste

# faccio classe specifica di wrap di s3 con try/catch per ciascun metodo
# faccio classe specifica di wrap di posix con try/catch per ciascun metodo
# faccio provino di uso di wrap s3
# faccio provino di uso di wrap posix
# test con nomi parametri espliciti
# se ok, creo pacchetto
#  https://dev.to/rf_schubert/how-to-create-a-pip-package-and-host-on-private-github-repo-58pa
#  o
#  https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

# autopep8 --in-place --aggressive --aggressive file.py

import os

from dotenv import load_dotenv

from fs import open_fs
from fs.base import FS
from fs.copy import copy_file

load_dotenv(override=True)

s3_fs = open_fs(
    's3://{}:{}@{}'.format(
        os.getenv('AWS_ACCESS_KEY_ID'),
        os.getenv('AWS_SECRET_ACCESS_KEY'),
        os.getenv('AWS_BUCKET')
    )
)

#
# write
#
with open('{}bbb'.format(os.getenv('FS_PATH_LOCAL')), 'rb') as read_file:
    s3_fs.upload('bbb', read_file) # copy LOCAL/bbb to s3://bbb

s3_fs.writebytes('mbytes', b"some initial binary data: \x00\x01")

#
# read
#
copy_file(s3_fs, 'bbb', './', '{}ccc'.format(os.getenv('FS_PATH_LOCAL'))) # copy s3://bbb to LOCAL/ccc
# TODO following on success
os_fs = open_fs('osfs://.')
with os_fs.open('{}ccc'.format(os.getenv('FS_PATH_LOCAL'))) as local_file:
    print(local_file.read()) # future: return

#
# md5
#
info = s3_fs.getinfo('bbb', namespaces=['s3'])
# TODO return
print(info.raw['s3']['e_tag'][1:-1])