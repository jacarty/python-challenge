# http://www.pythonchallenge.com/pc/def/274877906944.html

"""Challenge two in the python challenge"""

from itertools import izip as zip

alphabet = 'abcdefghijklmnopqrstuvwxyz'
substitution = 'cdefghijklmnopqrstuvwxyzab'
code = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
            bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
            sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
decoded = []


def challenge_2():

    dic = {k: v for k, v in zip(list(alphabet), list(substitution))}

    for each_letter in code:
        new = dic.get(each_letter, ' ')
        decoded.append(new)

    print ''.join(decoded)

if __name__ == '__main__':
    challenge_2()
