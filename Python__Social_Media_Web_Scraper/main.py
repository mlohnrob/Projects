import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://www.instagram.com/augustemmeryfunch/").read()


parsed_html = BeautifulSoup(html, features="html.parser")

followers = parsed_html.body.find('scripttype="application/ld+json"')
print(followers)
