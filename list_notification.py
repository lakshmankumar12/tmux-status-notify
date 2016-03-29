#!/usr/local/bin/python2.7

from __future__ import print_function
import fcntl

file="/home/lnara002/.notifications"

notif_file  = "/home/lnara002/.tmux_inform_notifications"
historical  = "/home/lnara002/.tmux_inform_notifications.historic"

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

