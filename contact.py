from flask import Flask,jsonify,request

app = Flask(__name__)


Data = [
    {     
        'id': 1,
        'Name': u'Ani',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Rumi',
        'Contact': u'9876543222', 
        'done': False
    }
]


@app.route("/add-data", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Wrong data provided.Please provide the correct data."
        },400) 
    contact = {
        'id': Data[-1]['id'] + 1,
        'Name' : request.json['Name'],
        'Contact' : request.json.get('Contact', ""), 
        'done': False
    }
    data.append(contact)
    return jsonify({
        "status" : "Success",
        "message" : "Yayy!Contact added successfully."
        })

@app.route("/get-data")

def get_task():
     return jsonify({
        'data' : Data
        })
 

if (__name__ == '__main__'):
    app.run(debug = True)