import sys
from sysargv import SysArgv
from replacer import WordReplacer


if __name__=='__main__':
    # print(sys.argv[1:])
    # with open('out.txt','w') as file:
    #     for arg in sys.argv[1:]:
    #         file.write(arg)
    if sys.argv[1:][0]=='-h':
        print('1:Path to directory with database and exe script\n2:id template\n3:Full path to new file')
    else:
        argv = SysArgv(sys.argv[1:])
        replace = WordReplacer(argv)