
fss3wrap
========

A python class to wrap `fs <https://github.com/PyFilesystem/pyfilesystem2>`_ and `fs-s3fs-ng <https://github.com/mrk-its/s3fs>`_.

With this library, you can use the same code to interact with a traditional file system or an AWS S3 bucket.
Its interface class exposes 7 common methods, not every single file system operation, of course.

It is still in its early stage of development so handle with care. 😃

Installation
------------

.. code-block::

   pip3 install fss3wrap

Usage
-----

Use the ``env_example`` and create your own ``.env`` file (or put the same variables in your environment in some other way), then set ``AWS_S3_USED`` to ``True`` or ``False`` as you need it: once in your script with a single class or use it with two ``Afs`` classes.

Env files are not read directly: they are used for testing purposes, it's user duty to call methods with proper values, with or without envs.

You can use the `test file <https://github.com/carlok/fss3wrap>`_ on GitHub as documentation of the methods.

Afs interface class methods
---------------------------


* ``bytes_write(destination_path, destination_file, mbytes)``
* ``directory_list(path)``
* ``download(relative_source_path, destination_path, filename, mode)``
* ``file_copy(source_path, source_file)``
* ``file_descriptor_copy(source_file_descriptor, destination_path, destination_file)``
* ``file_fd(file_path, file_name)``
* ``file_fd_bin(file_path, file_name)``
* ``file_md5(file_path, file_name)``
* ``file_read(source_path, source_file)``
* ``file_read_bin(source_path, source_file)``
* ``file_remove(file_path, file_name)``
* ``reinit(s3_used, s3_parameters, bucket, rootdir)``

A note on the tests
-------------------

Files needed to begin:


* ``local/LICENSE`` (text)
* ``local/extra_sub_folder/4x4.jpg`` (binary)
* ``local/extra_sub_folder/out_LICENSE`` (text)
* ``remote/extra_sub_folder/4x4.jpg`` (binary)
* ``remote/extra_sub_folder/out_LICENSE`` (text)
* ``remote_reinit/extra_sub_folder/4x4.jpg`` (binary)
* ``remote_reinit/extra_sub_folder/out_LICENSE`` (text)
  and two AWS S3 Bucket

Author
------

`Carlo Perassi <https://carlo.perassi.com>`_

Contributor
-----------

`Matteo Ferrabone <https://github.com/desmoteo>`_

Thanks
------


* `Kiwifarm Srl <https://www.kiwifarm.it/>`_
* `WaterView Srl <https://www.waterview.it/>`_
