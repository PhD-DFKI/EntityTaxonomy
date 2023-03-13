from nltk.corpus import wordnet as wn

word_synsets = wn.synsets('Train', wn.NOUN)
print('hello')
for ss in word_synsets:
    hyper = lambda s: s.hypernyms()
    print(list(ss.closure(hyper)))
    # to print only the first hypernym for each synset
    #for hyper in ss.hypernyms():
    #    print(ss, hyper)





