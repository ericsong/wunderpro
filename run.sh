#!/bin/bash
celery -A tasks worker --beat --loglevel=info
