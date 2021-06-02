#!/usr/bin/python3
import platform
import os
import sys

cwd = '/'.join((__file__).split('/')[:-1])
print(os.environ)
print(cwd)
if platform.system() == 'Darwin':
  os.environ['PYTHONHOME'] = cwd + '/macos'
  os.execv(cwd + '/macos/bin/python3.7', sys.argv)
else:
  os.environ['PYTHONHOME'] = cwd + '/linux'
  os.execv(cwd + '/linux/bin/python3.7', sys.argv)
