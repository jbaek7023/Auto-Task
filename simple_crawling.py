## Normal HTML Rendering
import requests
from bs4 import BeautifulSoup

html = request.get('https://askdjango.github.io/lv1/').Text
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('#course_list > .course > a'):
    print(tag.text, tag['href'])

## Ajax Rendering
import requests

course_list = requests.get('https://askdjango.github.io/lv2/data.json').json()
for course in course_list:
    print(course['name'], course['url'])

## Javascript Rendering Crawling
## Later
