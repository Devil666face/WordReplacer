import sys
from sysargv import SysArgv
from replacer import WordReplacer


if __name__=='__main__':
    argv = SysArgv(sys.argv[1:])
    replace = WordReplacer(argv)