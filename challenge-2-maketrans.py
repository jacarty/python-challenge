# http://www.pythonchallenge.com/pc/def/0.html

"""Challenge two in the python challenge"""

from string import maketrans
import webbrowser

alphabet = 'abcdefghijklmnopqrstuvwxyz'
substitution = 'cdefghijklmnopqrstuvwxyzab'
code = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
            bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
            sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

url = 'map'


def challenge_2():

    translation = maketrans(alphabet, substitution)
    print code.translate(translation)
    m = url.translate(translation)
    new_url = 'http://www.pythonchallenge.com/pc/def/'+m+'.html'
    webbrowser.open_new_tab(new_url)

if __name__ == '__main__':
    challenge_2()
