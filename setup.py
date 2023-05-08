from setuptools import setup

install_requires = [
    "jgo>=0.4.0",
]

entry_points = {
    "console_scripts": [
        "mobie=mobie:main",
    ]
}

version = "4.0.3"

classifiers = [
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 3 :: Only",
]

package_urls = {
    "Documentation": "https://mobie.github.io/",
}

setup(
    name="mobie",
    version=version,
    license_files=("LICENSE.txt",),
    author="Christian Tischer",
    author_email="christian.tischer@embl.de",
    maintainer="Christian Tischer",
    maintainer_email="christian.tischer@embl.de",
    description="Viewer for big multi-modal image data",
    url="https://github.com/mobie/mobie-viewer-fiji",
    package_urls=package_urls,
    packages=["mobie"],
    entry_points=entry_points,
    install_requires=install_requires,
    classifiers=classifiers,
)
