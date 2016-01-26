import string
import json

def createCeleryTaskConfig(config):
    config['args'] = json.dumps(config['args'])
    template =  string.Template("""
    '${title}': {
        'task': 'tasks.${type}',
        'schedule': tasks.${schedule},
        'args': ${args}
    },
    """)

    return template.substitute(config)

def createConfigFile(taskConfigs):
    lines = open('config.template', 'r').readlines()
    for config in taskConfigs:
        lines.insert(12, createCeleryTaskConfig(config))

    print "".join(lines)
