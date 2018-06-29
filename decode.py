#!/usr/bin/python
import sys
sOut = ""
for s in sys.argv[1].lower():
    if ord(s) < ord('g'):
     sOut += s
    else:
     sOut += str(ord(s)-ord('g'))

print sOut
