__author__ = 'ansha'

import sys

def prime(n) : # n is an argument. find if n is prime or not
    i = 2  # start loop with 2
    while i < n:

        print "i =", i
        if n % i == 0: # mod
            print n, "is not prime"
            sys.exit() # stop script

        i = i + 1 # adding 1 to i

    print n, "is prime"


prime(7)  # find if 7 is prime
prime(6)  # find if 6 is prime
prime(11) # find if 11 is primt







