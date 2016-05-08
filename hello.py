import sys

def Welcome(argv):
    if( len(argv) == 1 ):
        print("Hello World!")
    else:
        for arg in sys.argv[1:]:
            print( "Hello",arg+"!")

Welcome(sys.argv)
