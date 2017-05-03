#!/usr/bin/python

from __future__ import print_function
import fcntl
import os

from os.path import expanduser
home = expanduser("~")

notif_file  = os.path.join(home,".tmux_inform_notifications")
historical  = os.path.join(home,".tmux_inform_notifications.historic")

f=open(notif_file,"r+")
h=open(historical,"a")
fcntl.flock(f, fcntl.LOCK_EX)
for i in f:
  print(i,end="")
  h.write(i)
h.close()
f.truncate(0)
fcntl.flock(f, fcntl.LOCK_UN)
f.close()

