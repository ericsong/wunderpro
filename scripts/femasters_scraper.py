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

      print(br.open('https://frontendmasters.com/courses/').read())
