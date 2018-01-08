import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_53593.json'
json_string = urllib.request.urlopen(url).read().decode()
json_dir = json.loads(json_string)
comment_sum = 0

for comment in json_dir['comments']:
    comment_sum = comment_sum + comment.get('count', 0)

print(comment_sum)
