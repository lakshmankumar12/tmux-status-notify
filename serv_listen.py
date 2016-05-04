#!/usr/local/bin/python2.7


from __future__ import print_function
import fcntl
import socket
import datetime

file="/home/lnara002/.notifications"
UDP_IP = "135.227.232.177"
UDP_PORT = 25000

notif_file  = "/home/lnara002/.tmux_inform_notifications"

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

