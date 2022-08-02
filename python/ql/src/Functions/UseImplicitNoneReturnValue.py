
import sys

def my_print(*args):
    print (args)

def main():
    if err := my_print(sys.argv):
        sys.exit(err)


#FIXED VERSION
def main():
    my_print(sys.argv)
    #The rest of the code can be removed as None as always false

