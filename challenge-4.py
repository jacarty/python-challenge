# http://www.pythonchallenge.com/pc/def/equality.html

"""Challenge 4 in the python challenge series"""

import requests
import re
import webbrowser

get_text = re.compile('<!--(.+)-->', re.DOTALL)
solve = re.compile('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')


def challenge_4():

    r = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
    nonsense = get_text.search(r.text).group().encode('utf-8')
    trim = solve.findall(nonsense)
    print ''.join(trim)

if __name__ == '__main__':
    challenge_4()
