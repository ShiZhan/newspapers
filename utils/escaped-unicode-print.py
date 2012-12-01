#!/usr/bin/python
import sys

if len(sys.argv) < 2:
    print "where is input escaped-unicode file?"
    exit(1)

with open(sys.argv[1]) as f:
    str = f.read().decode('unicode_escape')
    print str.encode('utf-8')
