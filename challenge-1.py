# http://www.pythonchallenge.com/pc/def/0.html

"""Challenge one in the python challenge"""

import re
import webbrowser

url = 'http://www.pythonchallenge.com/pc/def/0.html'
ro = re.compile('\D+')


def challenge_1():

    page_number = 2 ** 38
    replace = ro.search(url).group()
    new_url = replace+str(page_number)+'.html'
    print new_url
    webbrowser.open_new_tab(new_url)

if __name__ == '__main__':
    challenge_1()
