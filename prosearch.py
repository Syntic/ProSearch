__author__ = 'Peter'

import urllib.request
import urllib.error
import json
import os
import InfoGrab
import time
import sys


def getPlayerFast(textfile):
    file = open(textfile, 'r')

    for line in file:
        list = line.split()

        acct = list[0]
        name = list[1]

        print('getMatches(' + acct + ',' + name + ')')
        getMatches(acct, name)


def getMatches(accountID, name, startID='99999999999'):
    # Download URL and save to String
    print(
        'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=28F7466B927B45E79E7C60E044E6B4CA&account_id=' + accountID + '&start_at_match_id=' + startID)

    try:
        response = urllib.request.urlopen(
            'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=28F7466B927B45E79E7C60E044E6B4CA&account_id=' + accountID + '&start_at_match_id=' + startID)
        html = response.read().decode("utf-8")

        if (json.loads(html)['result']['status'] == 1 and
                    len(json.loads(html)['result']['matches']) != 0):

            # JSON Search and list
            matches = json.loads(html)['result']['matches']

            # Make ID-only list
            allID = []
            for i in matches:
                allID.append(i['match_id'])

            #Create folder, create/open text file and print the list in it

            if not os.path.exists(os.getcwd() + '/me'):
                os.makedirs(os.getcwd() + '/me')
            if not os.path.exists(os.getcwd() + '/me/' + name + '_' + accountID + '.txt'):
                textfile = open(os.getcwd() + '/me/' + name + '_' + accountID + '.txt', 'a')

                for item in allID:
                    textfile.write("%s\n" % item)

                textfile.close()

            #Set new Start ID
            #print('Last Match ID ' + matches[-1])
            newID = (int(allID[-1])) - 1
            #print('New start ID ' + str(newID))


            # Execute again
            getMatches(accountID, name, str(newID))
    except urllib.error.URLError as e:
        print('Error while fetching site! Sleeping for 5 sec. and trying again...')
        print(e)
        time.sleep(5)
        getMatches(accountID, name, str(startID))


from os import listdir
from os.path import isfile, join


def comp(file):
    mypath = os.getcwd() + '/me/' + file
    propath = os.getcwd() + '/pros/'

    onlyfiles = [f for f in listdir(propath) if isfile(join(propath, f))]

    print(file + ' has played with these Pro Players:')
    print('----------------------------------------')

    for val in onlyfiles:
        compPro(mypath, propath + val)


def compPro(me, pro):
    file1 = open(pro, 'r')
    file2 = open(me, 'r')

    list1 = [line.split() for line in file1.readlines()]
    list2 = [line.split() for line in file2.readlines()]

    for val in list1:
        if val in list2:
            print(pro, val)


# ---------------------FIRST RUN--------------------------------------
# ---------------------FIRST RUN--------------------------------------
# ---------------------FIRST RUN--------------------------------------

# Ask for ID
givenID = input('Enter your ID: ')

# Set user path
path = os.getcwd() + '/me/'

# Search for name&file
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for val in onlyfiles:
    file = val
    temp = val.split('_')

    accID = temp[1]
    accID = accID[:-4]

    if accID == givenID:
        print('User found: ' + file)
        comp(file)
        wait = input('Press Enter to exit')
        sys.exit()

print('User not found locally. Choose your download:')
print('1. Get full match history (slow)')
print('2. Get last 500 Matches (fast)')
print('3. Exit')

menuChoice = input('Enter the number: ')

if menuChoice == '1':
    print('Downloading your full match history... This may take a few minutes')
    name = InfoGrab.getName(givenID)
    InfoGrab.getPlayer(givenID, name)
    comp(name + '_' + givenID + '.txt')
    wait = input('Press Enter to exit')
    sys.exit()


if menuChoice == '2':
    name = InfoGrab.getName(givenID)
    print('Downloading ' + name + '\'s last 500 matches...')
    getMatches(givenID, name)
    comp(name + '_' + givenID + '.txt')
    wait = input('Press Enter to exit')
    sys.exit()

if menuChoice == '3':
    print('Bye!')
    sys.exit()


