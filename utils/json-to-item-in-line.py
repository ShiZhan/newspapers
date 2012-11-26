import json
import sys

json_file_name = sys.argv[1]
try:
    with open(json_file_name, mode='r') as json_file:
        items = json.loads(json_file.read())
        json_file.close()
except Exception, e:
    raise e

for item in items:
    print "%s" % item