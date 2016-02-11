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
    if 'args' in config:
        args_string = "'args': ["
        for arg in config['args']:
            if(type(arg) is bool):
                if(arg):
                    args_string = args_string + "True"
                else:
                    args_string = args_string + "False"
            elif(type(arg) is str):
                args_string += "'" + arg + "'"
            elif(type(arg) is unicode):
                args_string += "'" + arg.encode('ascii', 'ignore') + "'"

            args_string = args_string + ","

        args_string = args_string[:-1] + "]"
    else:
        args_string = ""

    config['args_string'] = args_string

    template =  string.Template("""
    '${title}': {
        'task': 'tasks.${type}',
        'schedule': ${schedule},
        ${args_string}
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
