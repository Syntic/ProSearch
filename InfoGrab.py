__author__ = 'Peter'

__author__ = 'Peter'

import urllib.request
import urllib
import re
import os
import time
import sys


def getPageNumber(accID):

    try:
        url = 'http://www.dotabuff.com/players/'+accID+'/matches'

        # add a header to define a custon User-Agent
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0' }

        req = urllib.request.Request(url, headers=hdr)
        html = urllib.request.urlopen(req).read().decode("utf-8")

        m = re.search('page=(\d+)">Last', html)
        lastMatch = (m.group(1))
        return lastMatch
    except:
        print("Error Detected in getPageNumber: Sleeping for 15 min. and reconnecting")
        print(sys.exc_info()[0])
        time.sleep(900)
        getPageNumber(accID)



def pageGrab(accID, pageNumber, name):

    try:
        # Generate new URL
        url='http://www.dotabuff.com/players/'+accID+'/matches?page='+pageNumber

        # add a header to define a custon User-Agent
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0' }

        req = urllib.request.Request(url, headers=hdr)
        html = urllib.request.urlopen(req).read().decode("utf-8")

        # Find all match IDs
        newm = re.findall('(/matches/)(\d+)', html)
        m = list(set(newm))

        # Write to Text File
        if not os.path.exists(os.getcwd()+'/pros'):
            os.makedirs(os.getcwd()+'/pros')

        textfile = open(os.getcwd()+'/pros/'+name+'.txt', 'a')

        for match in m:
            textfile.write("%s\n" % match[1])

        textfile.close()

        time.sleep(5)
    except Exception as e:
        print("Error Detected in pageGrab(): Sleeping for 10 min. and reconnecting")
        print(sys.exc_info()[0])
        time.sleep(600)
        print(str(e))
        pageGrab(accID, pageNumber, name)
        print("Regrabbing page #"+pageNumber)

def getPlayer(accID,name):

    pages = getPageNumber(accID)
    pages = int(pages)

    for i in range(1, pages):
        print(i)
        pageGrab(str(accID), str(i), name)


