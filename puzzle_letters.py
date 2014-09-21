#!C:\\python27
# -*- coding: cp936 -*-
#Filename: puzzle_letters.py
import nltk
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
print [i for i in range(1,5)]##在脚本里面必须把print打上
print [w for w in wordlist if len(w) >= 6 and obligatory in w and nltk.FreqDist(w) <= puzzle_letters]
