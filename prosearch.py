__author__ = 'Peter'

import urllib.request
import json
import os

def getMatches(accountID,name,startID='99999999999'):

 #Download URL and save to String
    #print('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=28F7466B927B45E79E7C60E044E6B4CA&account_id=' + accountID + '&start_at_match_id='+startID)
    response = urllib.request.urlopen('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=28F7466B927B45E79E7C60E044E6B4CA&account_id=' + accountID + '&start_at_match_id='+startID)
    html = response.read().decode("utf-8")

    if (json.loads(html)['result']['status'] == 1 and
        len(json.loads(html)['result']['matches']) != 0):

        #JSON Search and list
        matches = json.loads(html)['result']['matches']

        #Make ID-only list
        allID =[]
        for i in matches:
            allID.append(i['match_id'])

        #Create folder, create/open text file and print the list in it

        if not os.path.exists(os.getcwd()+'/me'):
            os.makedirs(os.getcwd()+'/me')
        if not os.path.exists(os.getcwd()+'/me/'+name+'.txt'):
            textfile = open(os.getcwd()+'/me/'+name+'.txt', 'a')

            for item in allID:
                textfile.write("%s\n" % item)

            textfile.close()

        #Set new Start ID
        #print('Last Match ID ' + matches[-1])
        newID = (int(allID[-1]))-1
        #print('New start ID ' + str(newID))


        #Wait
        #print('Cycle Complete')

        #Execute again
        getMatches(accountID,name,str(newID))

from os import listdir
from os.path import isfile, join

def compPro(me,pro):
    file1 = open(pro,'r')
    file2 = open(me,'r')

    list1 = [line.split() for line in file1.readlines()]
    list2 = [line.split() for line in file2.readlines()]

    for val in list1:
        if val in list2:
            print(pro,val)


def comp(name):
    mypath = 'C:/Users/Peter/Documents/Pro Search/me/'+ name +'.txt'
    propath = 'C:/Users/Peter/Documents/Pro Search/promatches/'

    onlyfiles = [ f for f in listdir(propath) if isfile(join(propath,f)) ]

    print(name+' has played with these Pro Players:')
    print('----------------------------------------')

    for val in onlyfiles:
        compPro(mypath,propath+val)




