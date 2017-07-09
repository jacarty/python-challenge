# http://www.pythonchallenge.com/pc/def/linkedlist.php

"""Challenge 5 in the python challenge series"""

import requests

original_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
a = 0
b = 500


def challenge_5(url, x, y):

    while x <= y:
        r = requests.get(url)
        x += 1
        print r.text
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+r.text[24:]

if __name__ == '__main__':
    challenge_5(original_url, a, b)
