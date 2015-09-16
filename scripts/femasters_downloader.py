import os
import sys
import json
import urllib2

PARENT_DIR = 'Frontend Masters Courses'

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

def fakeDownloadFile(title, url):
    file_name = title + '.mp4'
    f = open(file_name.encode("utf-8"), 'wb')
    f.write('test')
    f.close()

courses = json.loads(open('courses.txt').read())
video_count = 0

os.makedirs(PARENT_DIR)
for course in courses:
    course_dir = os.path.join(PARENT_DIR, course['title'])
    os.makedirs(course_dir)
    for topic in course['topics']:
        link = topic['href']
        title = topic['title'].replace('/', '-')
        fakeDownloadFile(os.path.join(course_dir, title), link)
        topic['downloaded'] = True
