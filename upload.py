import urllib, urllib2
import json
from flask import Flask, request, redirect, url_for

with open('wunderlist_oauth.json') as data_file:
    oauth = json.load(data_file)

def push_to_api(push_url, payload, patch = False):
    headers = { 'X-Access-Token' : oauth['mytoken'], 'X-Client-ID' : oauth['client_id'], 'Content-Type' : 'application/json' }
    req = urllib2.Request(push_url, json.dumps(payload), headers)
    if patch:
      req.get_method = lambda: 'PATCH'
    return urllib2.urlopen(req).read()

def read_from_api(get_url, payload, patch = False):
    headers = { 'X-Access-Token' : oauth['mytoken'], 'X-Client-ID' : oauth['client_id'], 'Content-Type' : 'application/json' }
    req = urllib2.Request(get_url, json.dumps(payload), headers)
    if patch:
      req.get_method = lambda: 'PATCH'
    return urllib2.urlopen(req).read()

def addList(title):
    push_to_api('https://a.wunderlist.com/api/v1/lists', { 'title' : title })

def addTaskToDailyList(title):
    push_to_api('https://a.wunderlist.com/api/v1/tasks', { 'list_id': 83545841, 'title' : title })

def addTaskToInbox(title):
    push_to_api('https://a.wunderlist.com/api/v1/tasks', { 'list_id': 83545841, 'title' : title })

def getLists():
    data = get_from_api('https://a.wunderlist.com/api/v1/lists')
    print(data)
