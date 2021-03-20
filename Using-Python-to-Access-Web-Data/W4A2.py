__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


import urllib
from BeautifulSoup import *


def parser(url):

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    return tags

def pos_url(tags,position):
    count = 0
    for tag in tags:
         count += 1
         if count == position:
            url = str(tag.get('href',None))
            break
    name = []
    name_url = url.split('_')
    name.append(name_url[-1][:-5])
    return name, url

def main():
    url = raw_input('Enter URL: ')
    position = int(raw_input('Enter the position: '))
    count = int(raw_input('Enter count: '))
    print 'Retrieving: ' + url

    all_names = list()
    tags = parser(url)
    name,url = pos_url(tags,position)
    all_names.append(name)

    for i in range(count-1):
        tags = parser(url)
        name,url = pos_url(tags,position)
        print 'Retrieving: ' + url
        all_names.append(name)
    return all_names


print main()
