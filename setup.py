from setuptools import setup, find_packages
from boom import __version__
import sys

install_requires = ['moviepy',]

if sys.version_info < (2, 7):
    install_requires += ['argparse']

description = ''

for file_ in ('README', 'CHANGES', 'CONTRIBUTORS'):
    with open('%s.rst' % file_) as f:
        description += f.read() + '\n\n'


classifiers = ["Development Status :: 5 - Production/Stable",
               "License :: OSI Approved :: Apache Software License",
               "Programming Language :: Python :: 3.5",
               "Programming Language :: Python :: 3.6",
               "Programming Language :: Python :: 3.7"]

setup(name='VideoConverter',
      url='https://github.com/muriithiderro/VideoConverter',
      description="Simple Commandline tool to convert videos to audio files",
      author="Muriithi Derrick",
      author_email="muriithiderrick56@gmail.com",
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers,
      test_suite='unittest2.collector',
      entry_points="""
      [console_scripts]
      videoconverter = videoconverter.videoconverter:main
      """)