Reload
------

This utility starts given program and reloads it whenever any file in current directory changes. 
Paths can be excluded by putting regular expressions matching them in .reloadignore file.

Installation::

    pip install reload

Usage::

	reload ./server.py

Usage from Python::

    reload_me("server")

