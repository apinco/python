# Get libraries for reading URLs
import urllib.request, urllib.parse, urllib.error
# Get library for parsing XML
import xml.etree.ElementTree as ET
# Open and read the url

# This is awful code and I would never write this for production, but
# as a learning lesson I wanted to see how this would behave
# counts = ET.fromstring(urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_53592.xml').read()).findall('.//count')
print(sum([int(count.text) for count in ET.fromstring(urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_53592.xml').read()).findall('.//count')]))
