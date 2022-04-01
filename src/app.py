from flask import Flask, jsonify, request, json
app = Flask(__name__)

@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def Todos():

   return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)