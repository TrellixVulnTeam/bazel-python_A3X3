#!/usr/bin/python3
import platform
import os
import sys
import subprocess

cwd = '/'.join((__file__).split('/')[:-1])
print(sys.argv[1:])
print(os.environ)
if platform.system() == 'Darwin':
  subprocess.run([cwd + '/macos/bin/python3.7'] + sys.argv[1:], env= {'PYTHONHOME': cwd + '/macos', 'PYTHONPATH': os.environ.get('PYTHONPATH') }, check=True)
else:
  subprocess.run([cwd + '/linux/bin/python3.7'] + sys.argv[1:], env= {'PYTHONHOME': cwd + '/linux', 'PYTHONPATH': os.environ.get('PYTHONPATH') }, check=True)
