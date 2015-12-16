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
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour='5,18'),
        'args': ["measure weight"]
    },
        'add-read-chess-tactics-task': {
        'task': 'tasks.checkAndAddChessTacticsTask',
        'schedule': crontab(minute=0, hour=5, day_of_week='mon,thu,sat')
    },
        'add-read-js-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=12, day_of_week='fri'),
        'args': ["read js email"]
    },
        'add-send-tutor-email-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=5, day_of_week='fri'),
        'args': ["send tutor email"]
    },
        'add-casualharmony-report-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=20, day_of_week='tuesday,sunday'),
        'args': ["post casual harmony rehearsal report"]
    },
        'add-water-mint-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=20, day_of_week='sunday,thursday'),
        'args': ["water mint plant"]
    },
        'add-dotfiles-config-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=5),
        'args': ["code something! make a commit"]
    }
}

CELERY_TIMEZONE = 'EST'
