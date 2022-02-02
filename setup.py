import os

from setuptools import setup  # type: ignore


def find_stubs(package):
    stubs = []
    for root, _, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return stubs


with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="beancount-stubs",
    version="0.1.3",
    description="Stub files for the beancount package",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["beancount-stubs"],
    package_data={
        "beancount-stubs": find_stubs("beancount-stubs"),
    },
    author="Joshua Gilman",
    author_email="joshuagilman@gmail.com",
    url="https://github.com/jmgilman/beancount-stubs",
    keywords=["beancount", "stubs", "mypy", "types"],
    license="MIT",
    install_requires=["beancount>=2.3.4"],
    python_requires=">=3.8",
)
