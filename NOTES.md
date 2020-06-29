# Common commands 

```
pip3 install fs fs-s3fs-ng autopep8 pytest m2r twine python-dotenv wheel docutils===0.15
autopep8 --in-place --aggressive --recursive <folder>
pytest --cache-clear --color=yes --cov=fss3wrap/ -s -v
m2r README.md

python setup.py sdist bdist_wheel
twine upload dist/<last_tar.gz>
twine upload dist/<last_xxx-py3-none-any.whl>
```
