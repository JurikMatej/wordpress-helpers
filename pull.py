from ftplib import FTP
import sys
import json
import re
import os

def isDir(file):
  filePattern = re.compile('.+\..+')
  if filePattern.match(file):
    return False
  return True 
    
  
def downloadFile(file, _isDir):
  try:
    if not _isDir: # Base case: create a file and write downloaded content
      with open(file, 'wb') as f:
        ftp.retrbinary('RETR ' + str(file), f.write , blocksize=102400)
    else:          # Recursion: Traverse all subdirectories 
      os.mkdir(file)
      os.chdir(file)
      ftp.cwd(file)
      for nestedFile in ftp.nlst()[2:]:
        isNestedDir = isDir(nestedFile)
        downloadFile(nestedFile, isNestedDir)
      os.chdir('..')
      ftp.cwd('..')
    return
  except Exception as e:
    print(str(e))

# Get default arguments
with open('defaults.json', 'r') as defaults:
  print('Loading default arguments..')
  args = json.loads(defaults.read())

# Default save dir
args['dir'] = os.getcwd()

# Overwrite default args if any were specified via flags
print('Parsing flags...')
pattern = re.compile('--(.+)=(.*)')
for arg in sys.argv[1:]:
  if pattern.match(str(arg)):
    flag = pattern.search(str(arg))
    if flag.group(1) in args.keys():
      args[flag.group(1)] = flag.group(2)

# Connect to ftp with given credentials and download theme's files
print('Logging in..')
with FTP(args['host'], args['user'], args['passwd'], timeout=60) as ftp:
  ftp.cwd('web/wp-main/wp-content/themes/' + str(args['theme']))
  
  if os.path.exists(args['theme']):
    print('Overwriting existing files')
    from shutil import rmtree
    rmtree(args['theme'])
    os.mkdir(args['theme'])
  else:
    os.mkdir(args['theme'])
    
  os.chdir(args['theme'])

  print('Downloading...')
  for file in ftp.nlst()[2:]: 
    _isDir = isDir(file)
    print('Downloading ' + str(file))
    downloadFile(file, _isDir)

  ftp.quit()