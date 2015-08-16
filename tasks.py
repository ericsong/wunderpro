import urllib, urllib2
import json
from flask import Flask, request, redirect, url_for
from celery import Celery

app = Celery()
app.config_from_object('celeryconfig')

with open('wunderlist_oauth.json') as data_file:
    oauth = json.load(data_file)

def push_to_api(push_url, payload, patch = False):
    headers = { 'X-Access-Token' : oauth['mytoken'], 'X-Client-ID' : oauth['client_id'], 'Content-Type' : 'application/json' }
    req = urllib2.Request(push_url, json.dumps(payload), headers)
    if patch:
      req.get_method = lambda: 'PATCH'
    return urllib2.urlopen(req).read()

@app.task
def add(x, y):
    return x + y

@app.task
def addList(title):
    push_to_api('https://a.wunderlist.com/api/v1/lists', { 'title' : title })

@app.task
def addTaskToInbox(title):
    push_to_api('https://a.wunderlist.com/api/v1/tasks', { 'list_id': 103707402, 'title' : title })
