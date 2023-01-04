import subprocess
import tempfile
import os, sys
import platform
import time
import string
import random

opsys = platform.system()

def rand_name(length=10):
    characters = string.ascii_letters + string.digits
    name = ''.join(random.choice(characters) for i in range(length))
    return name

def pass_password(opsys = opsys):
    temp = tempfile.gettempdir()
    tmp_name = temp + os.sep + rand_name()
    modulepath = __file__[:-11]
    if opsys == 'Windows':
        subprocess.run(["start","/wait", "cmd", "/C", 'python', modulepath+'getpasswd.py', tmp_name], shell=True)
    elif opsys == 'Linux':
        os.system('gnome-terminal ' + '-- ' + 'python {}getpasswd.py {}; exit 0'.format(modulepath, tmp_name) +' -- wait ')
        while True:
            if os.path.exists(tmp_name):
                break
            else:
                time.sleep(.1)
    else:
        print('wrong Operationssystem')
        sys.exit(1)

    with open(tmp_name, 'r') as foo:
        pw = foo.readline()
    os.remove(tmp_name)
    return pw

class secret():
    '''object to save user and password - semi hidden'''
    
    def __init__(self):
        self.pw = pass_password()
        self.user = 'not specified'
    
    def user(self, x):
        '''define user name'''
        self.user = x
        
    def __repr__ (self):
        return 'user: {} \n  pw: {}'.format(self.user, '*'*5)
