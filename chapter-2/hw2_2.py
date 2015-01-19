import pymongo
import sys


# Copyright 2013, 10gen, Inc.
# Author: Andrew Erlichson


# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")



db = connection.students                 # attach to db
collection = db.grades         # specify the colllection


magic = 0

try:
    student_id = None
    iter = collection.find({'type':'homework'}).sort([("student_id", 1), ("score", 1)])
    for item in iter:
        if student_id != item['student_id']:
          collection.remove({'_id' : item['_id']})
          student_id = item['student_id']


except:
    print sys.exc_info()