import re
import pathlib
from _abbr import *


def loc(f):
    return pathlib.Path(__file__).parent.absolute() / f


__w_3_plus = re.compile('\w{3,}')
__w_ = re.compile('\w+')

names = set([x.strip() for x in (open(loc('names_decode.csv')).readlines())])
names = names | set([x[0] for x in hardcode])
# names from https://github.com/philipperemy/name-dataset


def name_preprocessing(z):
    z = z.lower().replace("'", '')
    z = z.replace('-redh', '').replace('-old', '').replace('-new', '')
    z = z.split('-pre')[0].split('-adr')[0].split('division of')[-1].split(
        'known as')[-1].split('-consolidated')[0]
    z = re.sub(r'(?=\w+)our\b', r'or', z)
    z = re.sub(r'(?=\w+)tt\b', r't', z)
    #  z = re.sub(r'(?=(\w+))([a-zA-Z])\2?',r'\2',z)
    z = re.sub(r'(?=\w+)er\b', r'ers', z)  # to not match e.g. glove vs glover
    z = z.replace('`', '').replace('& company', '').replace('& companies', '')
    z = re.sub(r'\bco\.? inc\b', r'inc', z)
    z = re.sub(r'\bco\.? ltd\b', r'inc', z)
    z = re.sub(r'\bthe\b', '', z)
    z = re.sub(r'\b[a-z]\.\b', '', z)
    z = re.sub(r'\bjr\.\b', '', z)
    z = re.sub(r'\bsr\.\b', '', z)
    z = ' '.join(re.findall(r'[\w\d]+', z))
    # combining single words...
    a = ''.join(re.findall(r'\b\w\s\b', z))
    if a:
        b = a.replace(' ', '')
        z = z.replace(a, b + ' ')

    #TODO: refactor the code to a function
    for string, adj_string in [
        ('i', ''),
        ('ii', ''),
        ('iii', ''),  #('iv',''),('v',''),
            #  ('vi',''),('vii',''),('viii',''),('ix',''),('x','')
    ]:
        if string.startswith('i'):
            continue
        z = re.sub('(?<!\w)' + string + '(?!\w)',
                   ' ' + adj_string,
                   z,
                   flags=re.IGNORECASE)
    ws = __w_.findall(z)
    counter = 0

    if len(ws) > 1:
        for w in ws:
            if w in names and len(w) > 1:
                counter += 1
    z = abbr_adj(z)

    if len(set([b for a, b in abbr if b != '']) & set(ws)) == 0:
        if counter >= 2:
            return
    return z.strip().lower()
