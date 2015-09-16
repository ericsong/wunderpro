import os
import sys
import requests
import json
import urllib2

def downloadFile(title, url):
    file_name = title + '.mp4'
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status

    f.close()

courses = json.loads(open('courses.txt').read())
video_count = 0

for course in courses:
    for topic in course['topics']:
        link = topic['href']
        title = topic['title']
        downloadFile(title, link)
        title['downloaded'] = True
        sys.exit(0)
    print course['title']
