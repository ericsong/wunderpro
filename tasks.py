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

def read_from_api(read_url):
    headers = { 'X-Access-Token' : oauth['mytoken'], 'X-Client-ID' : oauth['client_id'], 'Content-Type' : 'application/json' }
    req = urllib2.Request(read_url, {}, headers)
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

@app.task
def addChessTacticsTaskToInbox():
    ctfile = open('chesstactics_lessons.txt', 'r+b')
    lessons = ctfile.read().splitlines()

    for index in range(0, len(lessons)):
        line = lessons[index]
        sections = line.split(',')
        if sections[3] == '0':
            next_section = (sections[0], sections[1], sections[2])
            sections[3] = 1
            lessons[index] = ",".join(map(str, sections))
            break

    ctfile.seek(0)
    ctfile.write('\n'.join(lessons))

    next_section_str = next_section[0] + '.' + next_section[1] + '.' + next_section[2]
    task_title = 'read chess tactics ' + next_section_str
    push_to_api('https://a.wunderlist.com/api/v1/tasks', { 'list_id': 103707402, 'title' : task_title })
