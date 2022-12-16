#!/bin/ash


usr/bin/dbus-daemon  --config-file=/usr/share/dbus-1/system.conf --print-address 
/usr/bin/python3 /app/pa-captive-script.py
