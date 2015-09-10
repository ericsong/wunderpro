import os
import sys
import mechanize
import cookielib
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

# The site we will navigate into, handling it's session
br.open('https://frontendmasters.com/login')

course_links = []

# View available forms
for f in br.forms():
    print f

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
        course_links.append(link.get('href'))

for link in course_links:
    data = br.open(link).read()
    soup = BeautifulSoup(data)

    topics = []
    for topic in soup.select('li.video-nav-item a.video-link'):
        topic_link = topic.get('href')
        topic_title = topic.select('span.title')[0].getText()
        topics.append((topic_link, topic_title))

    for topic in topics:
        topic_url = link + topic[0]
        #data = br.open('https://frontendmasters.com/courses/organizing-javascript/#v=905ut58g8k').read()
        data = br.open('https://fast.wistia.com/embed/medias/905ut58g8k.json?callback=wistiajson1').read()
        print data
        soup = BeautifulSoup(data)
        source = soup.select('source')[0].get('src')
        print source
        sys.exit(1)

    sys.exit(1)
