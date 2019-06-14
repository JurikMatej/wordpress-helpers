from ftplib import FTP
import sys
import json
import re
import os

# Get default arguments
with open('defaults.json', 'r') as default:
  args = json.loads(default.read())

# Default save dir
args['dir'] = os.getcwd()

# Overwrite default args if any were specified via flags
pattern = re.compile('--(.+)=(.*)')
for arg in sys.argv[1:]:
  if pattern.match(str(arg)):
    flag = pattern.search(str(arg))
    if flag.group(1) in args.keys():
      args[flag.group(1)] = flag.group(2)

# Connect to ftp with given credentials and download theme's files
# conn = FTP(args[0], args[1], args[2], timeout=60)
