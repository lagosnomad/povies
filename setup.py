from setuptools import setup
import re
from setuptools import setup, find_packages

version = re.search(r'__version__\s*=\s*"(.+)"', open('povies/__init__.py', 'rt').read()).group(1)

setup(name='povies',
    version= version,
    description='Python wrapper for YTS.ag',
    classifiers = [
        # "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Version Control",
        "Topic :: Utilities"
    ],
    keywords=['yts', 'yify', 'torrent', 'torrents'],
    url='https://github.com/mczlatan/povies',
    author='McZlatan',
    author_email='bournethesonofthegun@gmail.com',
    license='GPLv3',
    packages=find_packages(exclude=['examples', 'tests']),
    install_requires=[
        'requests',
    ],
    # test_suite='nose.collector',
    # tests_require=['nose', 'nose-cover3'],
    # entry_points={
    #     'console_scripts': ['funniest-joke=funniest.command_line:main'],
    # },
    include_package_data=True,
    zip_safe=False)