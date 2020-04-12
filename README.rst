
fss3wrap
========

A python class to wrap `fs <https://github.com/PyFilesystem/pyfilesystem2>`_ and `fs-s3fs <https://github.com/PyFilesystem/s3fs>`_.

With this library, you can use the same code to interact with a traditional file system or an AWS S3 bucket.
Its interface class exposes 7 common methods, not every single file system operation, of course.

It is still in its early stage of development so handle with care. 😃

Installation
------------

.. code-block::

   pip3 install fss3wrap

Usage
-----

Use the ``env_example`` and create your own ``.env`` file (or put the same variables in your environment in some other way), then set ``AWS_S3_USED`` to ``True`` or ``False`` as you need it: once in your script with a single class or use it with two ``Afs`` classes

You can use the `test file <https://github.com/carlok/fss3wrap>`_ on GitHub as a documentation of the methods.

Afs interface class methods
---------------------------


* ``bytes_write(destination_path, destination_file, mbytes)``
* ``directory_list(path)``
* ``file_copy(source_path, source_file, destination_path, destination_file)``
* ``file_descriptor_copy(source_file_descriptor, destination_path, destination_file)``
* ``file_remove(file_path, file_name)``
* ``file_md5(file_path, file_name)``
* ``file_read(source_path, source_file, destination_path, destination_file)``

A note on the tests
-------------------

Files needed to begin:


* ``local/LICENSE``
* ``remote/out_LICENSE``
* ``remote/out2_LICENSE``

``local/`` is a local path, while ``remote/`` is a "remote" path, which is a normal folder in the OS file system case or a folder inside a bucket in the S3 case.

A few words on each test:


* ``test_bytes_write``\ : creates ``remote/out_LICENSE``
* ``test_directory_list``\ : lists ``remote/``
* ``test_filecopy``\ : copies ``local/LICENSE`` to ``remote/out_LICENSE``
* ``test_file_descriptor_copy``\ : same as ``test_filecopy`` but using a file descriptor
* ``test_file_remove``\ : deletes ``remote/out_LICENSE``
* ``test_file_md5``\ : returns the md5 string of ``remote/out2_LICENSE``
* ``test_file_read``\ : returns as a string the content of ``remote/out2_LICENSE`` after having copied it in ``local/LICENSE_from_remote``

Author
------

`Carlo Perassi <https://carlo.perassi.com>`_

Thanks
------


* `Kiwifarm Srl <https://www.kiwifarm.it/>`_
* `WaterView Srl <https://www.waterview.it/>`_
