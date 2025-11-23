import sys
import os

def   main( ):

    v = sys.version_info[0]
    if v==2:
        exec('print "Hello appsec world"')

    elif v==3:
        print("Hello appsec world")
    else:
        print("Unknown python version")




if __name__ == "__main__":
      main(   )
