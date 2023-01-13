from setuptools import setup
from distutils.command.build_py import build_py

import os

install_requires=[
    'jgo>=0.4.0',
]

entry_points={
    'console_scripts': [
        'mobie=mobie:launch_mobie',
#        'generate-mobie-bash-completion=mobie:generate_mobie_bash_completion'
    ]
}

name = 'mobie'
here = os.path.abspath(os.path.dirname(__file__))
version_info = {}
with open(os.path.join(here, name, 'version.py')) as fp:
    exec(fp.read(), version_info)
version = version_info['_mobie_version']

setup(
    name=name,
    version=version.python_version(),
    author='Christian Tischer',
    author_email='christian.tischer@embl.de',
    maintainer="Christian Tischer",
    maintainer_email="christian.tischer@embl.de",
    description='mobie',
    url='https://github.com/mobie/mobie-viewer-fiji',
    packages=['mobie'],
    entry_points=entry_points,
    install_requires=install_requires)
