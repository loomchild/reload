#!/usr/bin/env python

import sys
from reload import reload_me

if (len(sys.argv) > 1 and sys.argv[1] == "-r"):
    reload_me()
else:
    print("reload test")

