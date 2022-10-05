import os
from collections import Counter

from gensim.corpora import Dictionary
from gensim.utils import simple_preprocess
from itertools import islice

counts = Counter()
N = 1000
dictionary = Dictionary()

with open("en_wiki.txt", "r") as ifile:
    while True:
        lines500 = list(islice(ifile, N))
        if not lines500:
            break
        text = " ".join(lines500)
        tokens = simple_preprocess(text, max_len=25)
        dictionary.add_documents([tokens])
        # counts.update(tokens)


dictionary.filter_extremes(keep_n=5000000)
# counter = counts.most_common(1000000)
n_words = len(dictionary.token2id)
# n_words = len(counter)
os.makedirs("dictionary", exist_ok=True)
with open("dictionary/frequency_dictionary.txt", "w") as writer:
    for i in range(n_words):
        writer.write('{} {}\n'.format(dictionary[i], dictionary.cfs[i]))

#
# with open("dictionary/frequency_dictionary.txt", "w") as writer:
#     for c in counter:
#         writer.write('{} {}\n'.format(c[0], c[1]))
