__author__ = 'synti_000'

import InfoGrab

file = open('01players.txt','r')

for line in file:
    list = line.split()

    acct = list[0]
    name = list[1]

    print('getPlayer('+acct+','+name+')')
    InfoGrab.getPlayer(acct,name)