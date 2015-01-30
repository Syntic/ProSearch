__author__ = 'synti_000'

import InfoGrab
import time

file = open('01playersalt.txt','r')

for line in file:
    list = line.split()

    acct = list[0]
    name = list[1]

    print(acct)
    print(name)

    if name != 'skip':
        print('getMatches('+acct+','+name+')')
        InfoGrab.getPlayer(acct,name)
        time.sleep(60)

