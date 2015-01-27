import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")



db = connection.school                 # attach to db
collection = db.students         # specify the colllection


magic = 0

try:
    student_id = None
    students = collection.find()
    for student in students:
        # find the lowest score
        scores = student['scores']
        min_score = None
        for score in scores:
          if min_score == None and score['type'] == 'homework':
            min_score = score['score']
          if score['type'] == 'homework' and score['score'] < min_score:
            min_score = score['score']
        # remove it from array
        scores.remove({"type" : "homework", "score" : min_score})
        # update record
        student['scores'] = scores
        collection.update({"_id": student['_id'] }, student)


except:
    print sys.exc_info()