#!/usr/bin/python

from __future__ import print_function
import sys
import os
import socket
import subprocess
import re

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p","--pwd",  help="include pwd in message", action="store_true")
parser.add_argument("message",     help="message to send")
args = parser.parse_args()

message = args.message
if args.pwd:
  message = message + " from " + os.getcwd()
ip_proc=subprocess.Popen(["ip","route","get","8.8.8.8"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
line,err=ip_proc.communicate('')
errcode = ip_proc.wait()
if not line:
    print("Couldn't get ip route get 8.8.8.8 o/p")
    sys.exit(1)
match=re.search(r'src (\d+\.\d+\.\d+\.\d+)',line)
if not match:
    print("Count find src ip o/p")
ip=match.group(1)
port=25000
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(message, (ip, port))
