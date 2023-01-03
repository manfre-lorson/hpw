from getpass import getpass
import sys

tmp_name = sys.argv[1]


a = getpass('Enter password: ')
with open(tmp_name, 'w') as foo:
    foo.write(a)
sys.exit(0)