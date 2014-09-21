#!/usr/bin/python
# Filename: raising.py

import sys

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)# extend __init__ method from father to construct
        self.length = length
        self.atleast = atleast
while True:
    try:
        s = raw_input('Enter something -->')
        if len(s)<3:
            raise ShortInputException(len(s),3)
        print 'The program continues as usual.'
        break

    except EOFError:
        print '\nWhy did you do an EOF on me?'
        sys.exit()
    except ShortInputException, x:
        print 'ShortInputException: The input was of length %d, \
was expecting at least %d' %(x.length, x.atleast)

print 'No exception was raised.'
#sys.exit()
