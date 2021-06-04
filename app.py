from flask import Flask
app = Flask(__name__)
# @app.route("/")
# def helloWorld():
#     return "Hello World"
tasks = [{"id":1, "title":u"Buy Groceries", "description":u"milk,cheese,pizza,chips", "done":False},
{"id":2, "title":u"Learn Python", "description":u"Find a good python tutorial", "done":False}]
@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({"status":"error","message":"Data Not Found"}, 400)
    task = {"id":tasks[-1]["id"]+1, "title":request.json["title"], "description":request.json.get("description", ""),"done":False}
    tasks.append(task)
    return jsonify({"status":"success","message":"Task added successfully"})
@app.route("/get-data")
def get_task():
    return jsonify({data:tasks})
if __name__ == "__main__":
    app.run(debug = True)   
