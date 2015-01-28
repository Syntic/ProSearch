__author__ = 'Peter'

import prosearch

file = open('01players.txt','r')

for line in file:
    list = line.split()

    acct = list[0]
    name = list[1]

    print('getMatches('+acct+','+name+')')
    prosearch.getMatches(acct,name)
