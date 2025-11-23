import sys
import os

def   main( ):

    v = sys.version_info[0]
    if v==2:
        name = raw_input("Enter your name: ").strip()
        exec('print "Hello appsec world from " + name')

    elif v==3:
        name = input("Enter your name: ")
        print("Hello appsec world from " + name)
    else:
        print("Unknown python version")




if __name__ == "__main__":
      main(   )
