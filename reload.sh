#!/bin/bash

function ctrlc() {
	if [ -n "$PID" ]
	then
		kill $PID
	fi
	exit 0
}

trap ctrlc INT

if [ $# -eq 0 ]; then
	echo Specify command to run
	exit 1
fi

IGNORE_FILE=.reloadignore
IGNORE=""

if [ -f $IGNORE_FILE ]; then
	IGNORE=`echo $(cat .reloadignore) | tr " " "|"`
fi

echo Watching current directory, ignored file pattern: $IGNORE

INOTIFY_OPTS="-r -q -e modify"

if [ -n "$IGNORE" ]; then
	INOTIFY_OPTS="$INOTIFY_OPTS --exclude \"$IGNORE\""
fi

while true; do
  $@ &
  PID=$!
  inotifywait $INOTIFY_OPTS .
  disown $PID
  kill $PID
done

