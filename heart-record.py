from flask import Flask, jsonify, request
app = Flask(__name__)
heartRecords = [

    {
        "heart_id" : "1",
        "name" : "Ramos, Carlos Miguel A.",
        "date" : "September 21, 2022",
        "heart_rate" : "90/110"
    },

]

@app.route('/heartrecords', methods = ['GET'])
def getRecords():
    return jsonify(heartRecords)
@app.route('/heartrecords', methods = ['POST'])

def addRecord():
    heartRecord = request.get_json()
    heartRecords.append(heartRecord)
    return {'heart_id': len(heartRecords)}, 200

if __name__ == '__main__':
    app.run()
