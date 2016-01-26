import shutil
import string
import json
import datetime

OUTPUT_FILENAME = 'celeryconfig.py'

def backupConfig():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_filename = OUTPUT_FILENAME + '_' + timestamp + '.backup'
    shutil.copy(OUTPUT_FILENAME, backup_filename)

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

    backupConfig()

    outfile = open(OUTPUT_FILENAME, 'w')
    outfile.write("".join(lines))
