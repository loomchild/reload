#!/bin/bash

IGNORE_FILE=.reloadignore
IGNORE=""
SLEEP=1
SIGNAL="-SIGTERM"
#SIGNAL="-SIGINT"


function ctrlc() {
	if [ -n "$PID" ]
	then
		kill $SIGNAL $PID
	fi
	exit 0
}

trap ctrlc INT

if [ $# -eq 0 ]; then
	echo Specify command to run
	exit 1
fi

if [ -f $IGNORE_FILE ]; then
	IGNORE=`echo $(cat .reloadignore) | tr " " "|"`
fi

echo Watching current directory, ignored file pattern: $IGNORE

INOTIFY_OPTS="-r -q -e close_write"

if [ -n "$IGNORE" ]; then
	INOTIFY_OPTS="$INOTIFY_OPTS --exclude \"$IGNORE\""
fi

while true; do
  $@ &
  PID=$!
  inotifywait $INOTIFY_OPTS .
  disown $PID
  kill $SIGNAL $PID
  #sleep $SLEEP  #TODO: smart wait checking if process alive
done

