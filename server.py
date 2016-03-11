from flask import Flask, render_template, jsonify, send_from_directory, request
from config_extractor import getParsedTasks
from config_generator import createConfigFile
import json
import time, os
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

@app.route('/restartCelery')
def restartCelery():
    os.system("killall celery")
    os.system("celery -A tasks worker --beat --loglevel=info &")
    print("celery restarted...")
    return jsonify({'msg': 'sucess'})

@app.route('/createConfig', methods=["POST"])
def createConfig():
    tasks = json.loads(request.form['tasks'])

    print(tasks)
    createConfigFile(tasks)

    os.system("killall celery")
    os.system("celery -A tasks worker --beat --loglevel=info &")
    print("celery restarted...")

    return jsonify({'msg': "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
