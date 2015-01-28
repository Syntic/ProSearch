__author__ = 'Peter'

import InfoGrab


pages = InfoGrab.getPageNumber('70388657')
pages = int(pages)

for i in range(0, pages):
    print(i)
    print(InfoGrab.pageGrab('70388657', str(i), 'Dendi'))

