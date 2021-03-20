import urllib
from BeautifulSoup import *
def parser(url):
    #url = raw_input('Enter starting url:')
    #names = []
    #name_url = url.split('_')
    #names.append(name_url[-1][:-5])
    #print names
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    return tags

def pos_url(tags,position):
    count = 0
    for tag in tags:
         #print tag.get('href', None)
         count += 1
         if count == position:
            url = str(tag.get('href',None))
            break
    name = []
    name_url = url.split('_')
    name.append(name_url[-1][:-5])
    return name, url
url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
tag = parser(url)
n,url =  pos_url(tag,3)
print n