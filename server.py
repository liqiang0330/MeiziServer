from flask import Flask, request
import json
from bson import json_util
from bson.objectid import ObjectId
import pymongo

app = Flask(__name__)

mongoClient = pymongo.MongoClient('localhost', 27017)
db = mongoClient['dbmeizi']
def toJson(data):
    return json.dumps(data, default=json_util.default)

@app.route('/meizi', methods=['GET'])

def findmeizi():
    if request.method == 'GET':
        #lim = int(limit)
        #off = int(offset)
        results = db['meizi'].find().skip(0).limit(20)
        json_results= []
        for result in results:
            json_results.append(result)
        return toJson(json_results)

if __name__ == '__main__':
    app.run(debug=True)
