from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'rpc://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_ENABLE_UTC = True

CELERYBEAT_SCHEDULE = {
    'add-measure-weight-task': {
        'task': 'tasks.addTaskToDailyList',
        'schedule': crontab(minute=0, hour=5),
        'args': ["measure weight"]
    },
        'add-read-chess-tactics-task': {
        'task': 'tasks.addTaskToDailyList',
        'schedule': crontab(minute=0, hour=5),
        'args': ["read a section of chess tactics"]
    },
        'add-dotfiles-config-task': {
        'task': 'tasks.addTaskToDailyList',
        'schedule': crontab(minute=0, hour=5),
        'args': ["add something to dotfiles"]
    }
}

CELERY_TIMEZONE = 'EST'
