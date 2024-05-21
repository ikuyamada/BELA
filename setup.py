# Copyright (c) Meta Platforms, Inc. and affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from distutils.core import setup

from setuptools import find_packages

setup(
    name="bela",
    version="0.1",
    packages=find_packages(exclude=["mblink*"]),
    package_data={
        "bela": [
            "conf/**/*",
            "data/*",
            "tests/data/*",
        ]
    },
)
