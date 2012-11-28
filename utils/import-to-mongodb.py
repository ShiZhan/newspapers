import sys
import pymongo
import json

print "import crawled json file into mongodb 'newspapers' database."

if len(sys.argv) < 3:
    print "input as [collection] [json_file]"
    exit(1)

connection = pymongo.Connection("localhost", 27017)
news_database = connection.newspapers
news_collection = news_database[sys.argv[1]]

json_file_name = sys.argv[2]
try:
    with open(json_file_name, mode='r') as json_file:
        items = json.loads(json_file.read())
        json_file.close()
except Exception, e:
    raise e

for item in items:
    news_collection.save(item)

print len(items), " items saved to mongodb."
