def createCeleryTaskConfig(hasComma):
    return """
    'add-water-mint-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=20, day_of_week='sunday,thursday'),
        'args': [False, "water mint plant"]
    },
    """

def createConfigFile(tasks):
    lines = open('config.template', 'r').readlines()
    for task in tasks:
        lines.insert(12, task)

    print "".join(lines)

createConfigFile([createCeleryTaskConfig()])
