# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in supporting_system/__init__.py
from supporting_system import __version__ as version

setup(
	name='supporting_system',
	version=version,
	description='Track customer tickets and issues, maintain server levels and track response and resolutions',
	author='Momscode Technologies Pvt.ltd',
	author_email='info@momscode.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
