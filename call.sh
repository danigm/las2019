#!/bin/bash

DBUS=net.danigm.$1
OBJECT=/net/danigm/$1

echo "calling: $DBUS"
gdbus call --session --dest $DBUS --object-path $OBJECT --method $DBUS.test
