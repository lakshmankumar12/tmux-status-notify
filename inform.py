#!/usr/bin/python

import sys
import os
import socket

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p","--pwd",  help="include pwd in message", action="store_true")
parser.add_argument("message",     help="message to send")
args = parser.parse_args()

message = args.message
if args.pwd:
  message = message + " from " + os.getcwd()
ip1="135.227.232.199"
ip2="lakshmankumar.ddns.net"
port=25000
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(message, (ip1, port))
#sock.sendto(message, (ip2, port))
