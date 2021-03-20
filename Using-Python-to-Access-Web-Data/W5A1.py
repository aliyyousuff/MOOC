__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



import urllib
import xml.etree.ElementTree as ET


url = raw_input('Enter location: ')

print 'Retrieving ', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved ',len(data),' characters'

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
#print lst
numbers = []
for c in lst:
    #print 'Count', c.find('count').text
    numbers.append(int(c.find('count').text))
print 'Count:',len(numbers)
print 'Sum:', sum(numbers)
