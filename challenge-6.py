# http://www.pythonchallenge.com/pc/def/peak.html

"""Challenge 6 in the python challenge series"""

import pickle
from urllib import urlopen


def challenge_6():

    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    text = pickle.load(urlopen(url))

    for each_list in text:
        print "".join([key * value for key, value in each_list])

if __name__ == '__main__':
    challenge_6()
