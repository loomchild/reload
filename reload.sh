#!/bin/bash

function ctrlc() {
	if [ -n "$PID" ]
	then
		kill $PID
	fi
	exit 0
}

trap ctrlc INT


while true; do
  $@ &
  PID=$!
  inotifywait -r -q -e modify --exclude "\.(pyc|sw?|log)" .
  disown $PID
  kill $PID
done
