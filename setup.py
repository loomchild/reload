import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "reload",
    version = "0.1",
    author = "Jarek Lipski",
    author_email = "pub@loomchild.net",
    description = ("Reload a program if any file in current directory changes."),
    license = "MIT",
    keywords = "reload server",
    url = "https://github.com/loomchild/reload",
    py_modules=['reload'],
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["watchdog >=0.8"],
    entry_points={'console_scripts': [
        'reload = reload:main',
    ]},
)

