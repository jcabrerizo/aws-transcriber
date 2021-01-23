from setuptools import setup, find_packages

setup(
   name='AWS Transcriber',
   version='0.1.0',
   description='<DESCRIPTION>',
   author='Juan Cabrerizo',
   url="https://github.com/jcabrerizo/aws-transcriber",
   packages=find_packages(),
   entry_points={
       'console_scripts': ['transcriber = transcriber.__main__:main']
       }
) 