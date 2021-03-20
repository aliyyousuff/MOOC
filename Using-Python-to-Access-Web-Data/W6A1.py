__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'




import json
import urllib
#url = 'http://python-data.dr-chuck.net/comments_178655.json'
url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
#print data
info = json.loads(data)
#print info
numbers = []
print 'Retrieved ', len(data), 'characters'

for item in info['comments']:
    #print 'Name', item['name']
    #print 'count', item['count']
    numbers.append(int(item['count']))
print 'Count:',len(numbers)
print 'Sum: ',sum(numbers)
