#!/usr/bin/python3
import platform
import os
import sys

cwd = '/'.join((__file__).split('/')[:-1])

if platform.system() == 'Darwin':
  os.environ['PYTHONHOME'] = 'macos'
  os.execv(cwd + '/macos/bin/python3.7', sys.argv)
else:
  os.environ['PYTHONHOME'] = 'linux'
  os.execv(cwd + '/linux/bin/python3.7', sys.argv)
