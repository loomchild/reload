#!/usr/bin/env python

import sys, os, subprocess, time, signal, re, inotifyx



command = sys.argv[1:]
pid = 0

def ctrlc(signum, frame):
    if pid > 0:
        os.killpg(pid, signal.SIGKILL)
    exit(0)
    
signal.signal(signal.SIGINT, ctrlc)

include_pattern = re.compile('.*')
exclude_pattern = re.compile('.*\.(pyc|sw?|log)')

def check_file(name):
    include = include_pattern.match(name)
    exclude = exclude_pattern.match(name)
    return include and not exclude

def wait(fd):
    watch = inotifyx.add_watch(fd, '.', inotifyx.IN_MODIFY | inotifyx.IN_CREATE | inotifyx.IN_DELETE)
    match = False
    while not match:
        events = inotifyx.get_events(fd)
        for event in events:
            name = event.name
            if name and check_file(name):
                match = True
                break
    time.sleep(0.5)
    inotifyx.get_events(fd)
    inotifyx.rm_watch(fd, watch)


fd = inotifyx.init()

try:
    while True:
        pid = subprocess.Popen(command, preexec_fn=os.setsid).pid

        wait(fd)
        print "Kill'em all"

        os.killpg(pid, signal.SIGKILL)
        pid = 0

finally:
    os.close(fd)

# TODO: Add recursive
