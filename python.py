#!/usr/bin/python3
import platform
import os
import sys

if platform.system() == 'Darwin':
  os.environ['PYTHONHOME'] = 'macos'
  os.execv('macos/bin/python3.7', sys.argv)
else:
  os.environ['PYTHONHOME'] = 'linux'
  os.execv('linux/bin/python3.7', sys.argv)
