import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_53590.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find_all('span')
numbers = list()
for tag in tags:
    for number in tag.contents:
        numbers.append(int(number))
print(sum(numbers))