# this is a module -- i want to stop people executing it 

import sys
if __name__ == '__main__':
    sys.exit()


def myfunc():
    pass


print(__name__)

