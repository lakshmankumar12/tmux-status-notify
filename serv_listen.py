#!/usr/bin/python


from __future__ import print_function
import fcntl
import socket
import datetime
import os

UDP_IP = "0.0.0.0"
UDP_PORT = 25000

from os.path import expanduser
home = expanduser("~")
notif_file  = os.path.join(home,".tmux_inform_notifications")

def main():
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind((UDP_IP, UDP_PORT))
  while True:
    data, addr = sock.recvfrom(1024)
    data = data.strip('\n')
    f=open(notif_file,"a")
    fcntl.flock(f, fcntl.LOCK_EX)
    f.write("%s - %s\n"%(datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S"),data))
    print("%s - %s"%(datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S"),data))
    fcntl.flock(f, fcntl.LOCK_UN)
    f.close()

#main()
import daemon

with daemon.DaemonContext():
  main()

