#!/usr/bin/python3
import platform
import os
import sys
import subprocess

cwd = '/'.join((__file__).split('/')[:-1])
print(os.environ)
print(cwd)
if platform.system() == 'Darwin':
  subprocess.run([cwd + '/macos/bin/python3.7'] + sys.argv[1:], check=True)
else:
  subprocess.run([cwd + '/linux/bin/python3.7'] + sys.argv[1:], check=True)
