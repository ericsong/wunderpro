import string
import json

def stripQuotes(s):
    if s[0] == "'" and s[-1] == "'":
        return s[1:-1] 
    else: 
        return s

def stripComma(s):
    if s[-1] == ",":
        return s[:-1]
    else:
        return s

def getTasksFromConfig():
    lines = open('celeryconfig.py').readlines()

    tasks = []

    task = ""
    addLine = False

    for line in lines:
        if addLine:
            if '},' in line:
                tasks.append(task)
                task = ""
            else:
                task += line

        if 'CELERYBEAT_SCHEDULE' in line:
            addLine = True

        if 'CELERY_TIMEZONE' in line:
            addLine = False

    return tasks

def parseTask(task):
    lines = filter(None, task.split("\n"))
   
    config = {
        'title': lines[0].split("'")[1]
    }

    for line in lines[1:]:
        key = stripComma(stripQuotes(line.split(':', 1)[0].strip()))
        val = stripComma(stripQuotes(line.split(':', 1)[1].strip()))

        if key == 'task':
            val = val.split("'")[1].split('.')[1]
        elif key == 'args':
            val = eval(val)

        config[key] = val

    return config

for task in getTasksFromConfig():
    print(parseTask(task))
