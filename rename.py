__author__ = 'synti_000'

import os

# Set user path
path = os.getcwd() + '/pros2/'

# Search for name&file
onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for val in onlyfiles:
    name = val[:-4]

    file = open(os.getcwd() + '/01players.txt', 'r')

    for line in file:
        list = line.split()
        newName = list[1]
        accID = list[0]

        if newName == name:
            print('Match found '+ newName)
            os.rename(os.getcwd() + '/pros2/'+ val, os.getcwd() + '/pros2/'+name+'_'+accID+'.txt')
            print('Renamed from | '+val+' | to | ' +name+'_'+accID+'.txt')



