from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='',
    author='No Name',
    author_email='no_name@gmail.com',
    url='',
    license='',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': 
                  ['sortfolder = clean_folder.sort:main']}
) 