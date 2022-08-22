from gensim.corpora import Dictionary
from gensim.utils import simple_preprocess

dictionary = Dictionary()

with open("en_wiki.txt", "r") as ifile:
    for line in ifile:
        tokens = simple_preprocess(line)
        dictionary.add_documents([tokens])


dictionary.filter_extremes(keep_n=100000)

n_words = len(dictionary.token2id)
with open("data/frequency_dictionary.txt", "w") as writer:
    for i in range(n_words):
        writer.write('{} {}\n'.format(dictionary[i], dictionary.cfs[i]))
