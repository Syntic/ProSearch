__author__ = 'Peter'

import prosearch

#Download my last 500 Matches

accID = '20771881'
name = 'Atze'

prosearch.getMatches(accID,name)

#Compare to saved Database

prosearch.comp(name)
