import nltk
from nltk.util import ngrams

def word_grams(words, min=1, max=4):
    s = []
    for n in range(min, max):
        for ngram in ngrams(words, n):
            s.append(' '.join(str(i) for i in ngram))
    return s

bla = word_grams('one two three four'.split(' '))
print lm.prob("word", ["This is a context which generates a word"])
print (bla)