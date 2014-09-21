#!C:\\python27
#Filename: text_tools.py

from __future__ import division

##Return the vocabulary of the text
def vocab_size(text):
    print 'The vocabulary is',len(set([w.lower() for w in text if w.isalpha()]))

def percent(word,text):
    fdist=FreqDist(text)
    print 100*fdist[word]/len(text),'%'
