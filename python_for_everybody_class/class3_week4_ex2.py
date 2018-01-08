import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Phoenix.html"
count = input("Enter count: ")
position = input("Enter Position: ")

for i in range(int(count) + 1):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup.find_all('a')
    url = a_tags[int(position) - 1].get('href')

