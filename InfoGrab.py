__author__ = 'Syntic'

import urllib.request
import urllib
import re
import os
import time
import sys

def getPlayerList(textfile):

    #Open Text File
    file = open(textfile,'r')

    #Split every line into name+accountID
    for line in file:
        list = line.split()

        acct = list[0]
        name = list[1]

        print(acct+' '+name)

        if name != 'skip':
            print('getPlayer('+acct+','+name+')')
            getPlayer(acct,name)
            time.sleep(60)


def getPlayer(accID,name):

    #See if file already exists, if it does clear the file
    if os.path.exists(os.getcwd()+'/pros/'+name+'_'+accID+'.txt'):
        open(os.getcwd()+'/pros/'+name+'_'+accID+'.txt', 'w').close()

    #Get Page number
    pages = int(getPageNumber(accID))

    #cycle through all pages and grab info for them
    for i in range(1, pages):
        print(i)
        pageGrab(str(accID), str(i), name)



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


        textfile = open(os.getcwd()+'/pros/'+name+'_'+accID+'.txt', 'a')

        for match in m:
            textfile.write("%s\n" % match[1])

        textfile.close()

        time.sleep(5)
    except Exception as e:
        #Prevent Internet Problems or Request Refusals
        print("Error Detected in pageGrab(): Sleeping for 5 min. and reconnecting")
        print(sys.exc_info()[0])
        time.sleep(300)
        print(str(e))
        pageGrab(accID, pageNumber, name)
        print("Regrabbing page #"+pageNumber)

def getPageNumber(accID):

    try:
        url = 'http://www.dotabuff.com/players/'+accID+'/matches'

        # add a header to define a custon User-Agent
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0' }

        req = urllib.request.Request(url, headers=hdr)
        html = urllib.request.urlopen(req).read().decode("utf-8")

        #Regex Search the number on the page and return it
        m = re.search('page=(\d+)">Last', html)
        lastMatch = (m.group(1))
        return lastMatch

    except:
        #Prevent Internet Problems or Request Refusals
        print("Error Detected in getPageNumber: Sleeping for 5 min. and reconnecting")
        print(sys.exc_info()[0])
        time.sleep(300)
        getPageNumber(accID)


