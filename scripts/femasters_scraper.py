import os
import sys
import requests
import mechanize
import cookielib
import json
from bs4 import BeautifulSoup
import html2text

# Credentials
fem_user = os.environ['FEM_USER']
fem_pass = os.environ['FEM_PASS']

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

def getVideoLink(id):
    data = requests.get('https://fast.wistia.com/embed/medias/' + id + '.json', headers={"Referer": "https://frontendmasters.com/courses/"}).text
    parsed = json.loads(data)
    link = parsed['media']['assets']['original']['url']
    return link

# The site we will navigate into, handling it's session
br.open('https://frontendmasters.com/login')

course_links = []

# View available forms
for f in br.forms():
    # Select the second (index one) form (the first form is a search query box)
    br.select_form(nr=0)

    # User credentials
    br.form['rcp_user_login'] = fem_user
    br.form['rcp_user_pass'] = fem_pass

    # Login
    br.submit()

    data = br.open('https://frontendmasters.com/courses/').read()
    soup = BeautifulSoup(data)

    for link in soup.select('div.course-list-item-alt div.content h2.title a'):
        course_links.append((link.get('href'), link.getText()))

courses = []

for link in course_links:
    link, title = link
    data = br.open(link).read()
    soup = BeautifulSoup(data)

    topics = []
    for topic in soup.select('li.video-nav-item a.video-link'):
        topic_id = topic.get('href')[3:]
        topic_title = topic.select('span.title')[0].getText()
        topics.append({'id': topic_id, 'title': topic_title, 'downloaded': False})

    for topic in topics:
        video_href = getVideoLink(topic['id'])
        topic['href'] = video_href

    courses.append({'title': title, 'topics': topics})

print(json.dumps(courses))
