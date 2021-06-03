#!/usr/bin/python3
import platform
import os
import sys
import subprocess

cwd = '/'.join((__file__).split('/')[:-1])

if platform.system() == 'Darwin':
  subprocess.run([cwd + '/macos/bin/python3.7'] + sys.argv[1:], env= {'PYTHONHOME': cwd + '/macos' }, check=True)
else:
  subprocess.run([cwd + '/linux/bin/python3.7'] + sys.argv[1:], env= {'PYTHONHOME': cwd + '/linux' }, check=True)
