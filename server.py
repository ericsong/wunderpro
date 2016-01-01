from flask import Flask
from config_extractor import getParsedTasks
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    tasks = getParsedTasks()

    return json.dumps(tasks)

if __name__ == '__main__':
    app.run()
