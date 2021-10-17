import re
import pymorphy2 as pm


def CreateListOfWords(s):
    s=s.lower()
    s=' '+s+' '
    s=re.sub(r'(\s)(-)(\s)',r'\1\3',s)
    s=re.sub(r'([.,])(-)(\s)',r'\3',s)
    l=re.findall(r'[а-яА-ЯёЁ-]+',s)
    return l

def CreateListOfNormalForms(l,ma):
    return [ma.parse(x)[0].normal_form for x in l]


def CreateDictForDF(s,ma):
    l=CreateListOfNormalForms(CreateListOfWords(s),ma)
    S=set(l)
    L=sorted([(l.count(x),x) for x in S])
    d={'слово':[x[1] for x in L], 'количество вхождений':[x[0] for x in L]}
    return d

def CreateReverseDictForDF(s,ma):
    l=CreateListOfNormalForms(CreateListOfWords(s),ma)
    S=set(l)
    L=sorted([(l.count(x),x) for x in S],reverse=True)
    d={'слово':[x[1] for x in L], 'количество вхождений':[x[0] for x in L]}
    return d

def Test():
    pass

if __name__=='__main__':
    Test()
