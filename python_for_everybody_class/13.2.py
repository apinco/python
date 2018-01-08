import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = input("Enter location: ")
url = serviceurl + urllib.parse.urlencode({'address': address})

json_string = urllib.request.urlopen(url).read().decode()
json_dir = json.loads(json_string)

print(json_dir.get('results', [])[0].get('place_id', 'none'))
