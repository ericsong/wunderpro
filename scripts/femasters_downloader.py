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
        sys.stdout.write(status)
        sys.stdout.flush()

    f.close()

def fakeDownloadFile(title, url):
    file_name = title + '.mp4'
    f = open(file_name.encode("utf-8"), 'wb')
    f.write('test')
    f.close()

f = open('courses.txt', 'r+b')
courses = json.loads(f.read())

if not os.path.exists(PARENT_DIR):
    os.makedirs(PARENT_DIR)

for j in range(0, len(courses)):
    course = courses[j]
    course_dir = os.path.join(PARENT_DIR, course['title'])

    if not os.path.exists(course_dir):
        os.makedirs(course_dir)

    for i in range(0, len(course['topics'])):
        topic = course['topics'][i]

        if topic['downloaded']:
            continue

        link = topic['href']
        title = topic['title'].encode('ascii', 'ignore')#replace('/', '-')
        print title

        downloadFile(os.path.join(course_dir, title), link)
        topic['downloaded'] = True

        f.seek(0)
        f.write(json.dumps(courses))
        f.truncate()
