__author__ = 'heigo'

import subprocess, sys

result = subprocess.check_call('C:\python34\python Isikukood_kontrollnumber.py | clip', shell=True)
# print(result)
sys.exit(result)



