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
        'task': 'tasks.addSingleTaskToInbox',
        'schedule': crontab(minute=0, hour='5,18'),
        'args': "true,measure weight"
    },
    
    'add-read-chess-tactics-task': {
        'task': 'tasks.checkAndAddChessTacticsTask',
        'schedule': crontab(minute=0, hour=5, day_of_week='mon,thu,sat'),
        'args': ""
    },
    
    'add-read-js-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=12, day_of_week='fri'),
        'args': "true,read js email"
    },
    
    'add-send-tutor-email-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=17, day_of_week='fri'),
        'args': "true,send tutor email"
    },
    
    'add-drink-water-task': {
        'task': 'tasks.addSingleTaskToInbox',
        'schedule': crontab(minute=0, hour='12,16,20,0'),
        'args': "true,drink water"
    },
    
    'add-water-mint-task': {
        'task': 'tasks.addTaskToInbox',
        'schedule': crontab(minute=0, hour=20, day_of_week='sunday,thursday'),
        'args': "true,water mint plant"
    },
    }

CELERY_TIMEZONE = 'EST'
