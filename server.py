from flask import Flask, render_template, jsonify, send_from_directory, request
from config_extractor import getParsedTasks
import json
app = Flask(__name__, static_url_path='')
app.debug = True

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/tasks')
def getTasks():
    tasks = getParsedTasks()

    return jsonify(tasks = tasks)

@app.route('/createConfig', methods=["POST"])
def createConfig():
    print(json.loads(request.form['tasks'])[0]['title'])

    return jsonify({'msg': "hi"})

if __name__ == '__main__':
    app.run()
