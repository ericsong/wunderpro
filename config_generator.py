import string
import json

def createCeleryTaskConfig(config):
    config['args'] = json.dumps(config['args'])
    template =  string.Template("""
    '${title}': {
        'task': 'tasks.${taskType}',
        'schedule': tasks.${schedule},
        'args': ${args}
    },
    """)

    return template.substitute(config)

def createConfigFile(tasks):
    lines = open('config.template', 'r').readlines()
    for task in tasks:
        lines.insert(12, task)

    print "".join(lines)

tasks = []
mintConfig = {
    'title': 'add-water-mint-task',
    'taskType': 'addTaskToInbox',
    'schedule': 'crontab(minute=0, hour=20, day_of_week=\'sunday,thursday\')',
    'args': [False, "water mint plant"],
    'hasComma': False
}
tasks.append(createCeleryTaskConfig(mintConfig))

createConfigFile(tasks)
