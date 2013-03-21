#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.0.1"

setup(
    name="teensymail",
    version=version,
    description="An itty-bitty python email framework",
    classifiers=[
        ""
    ],
    keywords="mail smtp imap pop3",
    author="Alex Buie",
    author_email="alex.buie@frozenfeline.net",
    url="http://github.com/ab2525/teensymail",
    license="WTFPL/2.0",
    packages=find_packages(
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "none"
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)