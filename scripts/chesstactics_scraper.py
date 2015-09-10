from bs4 import BeautifulSoup

import requests

url = "http://www.chesstactics.org/toc/toc_right_expanded.php"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

read = '1'

for link in soup.select('tr td a.smallgraytext'):
  section_string = link.get('href').split('From')[1][1:][:-2]
  parsed = section_string.split(',')
  chapter, section, lesson = parsed

  if chapter == '2' and section == '1' and lesson == '9':
    read = '0'

  print(section_string + "," + read)
