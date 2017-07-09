# http://www.pythonchallenge.com/pc/def/ocr.html

"""Challenge 3 in the python challenge series"""

import requests
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'
find = re.compile('<!--\n%.+', re.DOTALL)


def challenge_3():

    r = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
    nonsense = find.search(r.text).group().encode('utf-8')

    for each_letter in nonsense:
        if each_letter in list(alphabet):
            print each_letter

if __name__ == '__main__':
    challenge_3()
