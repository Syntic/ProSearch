__author__ = 'Peter'

import urllib.request
import urllib
import re

url = 'http://www.dotabuff.com/players/70388657/matches'

# add a header to define a custon User-Agent
hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0' }

req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read().decode("utf-8")

m = re.findall('(/matches/)(\d+)', html)

for match in m:
    print(match[1])

