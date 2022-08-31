from gensim.corpora import Dictionary
from gensim.utils import simple_preprocess
from itertools import islice


N = 1000
dictionary = Dictionary()

with open("en_wiki.txt", "r") as ifile:
    while True:
        lines500 = list(islice(ifile, N))
        if not lines500:
            break
        text = " ".join(lines500)
        tokens = simple_preprocess(text)
        dictionary.add_documents([tokens])


dictionary.filter_extremes(keep_n=1000000)

n_words = len(dictionary.token2id)
with open("dictionary/frequency_dictionary.txt", "w") as writer:
    for i in range(n_words):
        writer.write('{} {}\n'.format(dictionary[i], dictionary.cfs[i]))
