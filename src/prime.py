__author__ = 'ansha'

import sys

n = 37 # find if n is prime
print n
i = 2  # start loop with 2
print i


while i < n:

    print "i =", i
    if n % i == 0: # mod
        print n, "is not prime"
        sys.exit() # stop script

    i = i + 1 # adding 1 to i

print n, "is prime"









