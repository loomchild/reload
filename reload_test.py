import sys
from reload import reload_me

if (len(sys.argv) > 1 and sys.argv[1] == "-r"):
    reload_me("-r")
else:
    print("reload test")

