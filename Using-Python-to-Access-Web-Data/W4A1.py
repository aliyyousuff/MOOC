__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


import urllib
from BeautifulSoup import *
import re

numbers = list()
import urllib
from BeautifulSoup import *
import re

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_178654.html ').read()
soup = BeautifulSoup(html)
tags = soup('span')        # separate data based on 'span' tag
for line in tags:
    line = str(line)
    line = line.rstrip()
    numbers.append(int(re.findall('[0-9]+',line)[0])) # keep only digit

print sum(numbers)