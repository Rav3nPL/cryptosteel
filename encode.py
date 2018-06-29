#!/usr/bin/python
import sys
sOut = ""
c = 0
for s in sys.argv[1].lower():
    if s.isalpha():
     sOut += s
    else:
     sOut += chr(ord('g')+int(s))
    c += 1
    if c%4 == 0:
     sOut += " "
print sOut.upper()
