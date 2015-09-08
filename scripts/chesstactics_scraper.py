from bs4 import BeautifulSoup

import requests

url = "http://www.chesstactics.org/toc/toc_right_expanded.php"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.select('tr td a.smallgraytext'):
  print(link.get('href').split('From')[1][1:])
