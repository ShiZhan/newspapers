import sys

with open(sys.argv[1]) as f:
  str = f.read().decode('unicode_escape')
  print str.encode('utf-8')