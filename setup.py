import os

from setuptools import setup  # type: ignore


def find_stubs(package):
    stubs = []
    for root, _, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return stubs


setup(
    packages=["beancount-stubs"],
    package_data={
        "beancount-stubs": find_stubs("beancount-stubs"),
    },
)
