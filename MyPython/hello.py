#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys
import pinky

# Gather our code in a main() function
def main1():
    print 'Hello there', sys.argv[1]


# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main1()
    name = 'mah'
    pinky.foo(name)
    print name
