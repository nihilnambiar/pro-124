from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        "Contact":"9987644456",
        "Name":"Raju",
        "done":False,
        "id":1

     },
    {
       "Contact":"9876543222",
        "Name":"Rahul",
        "done":False,
        "id":2
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
            
        },400)

contact={
    'id':tasks[-1]['id'] + 1,
    'Name':request.json['Name'],
    'Contact': request.json.get('Contact',""),
    'done':False
}