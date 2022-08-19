from collections import Counter
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
from gensim.models.phrases import Phrases, ENGLISH_CONNECTOR_WORDS

nlp = English()
tokenizer = Tokenizer(nlp.vocab)

bigram = Phrases(delimiter=" ",  min_count=5, threshold=10)
with open("en_wiki.txt", "r") as ifile:
    for line in ifile:
        sentence = [word.text for word in tokenizer(line.strip())]
        bigram.add_vocab([sentence])

bigram_model_counter = Counter()
for key in bigram.vocab.keys():
    if len(key.split(" ")) > 1:
        bigram_model_counter[key] += bigram.vocab[key]

# for key, counts in bigram_model_counter.most_common(50):
#     print('{} {}'.format(key, counts))

with open("frequency_bigramdictionary.txt", "w") as writer:
    for key, counts in bigram_model_counter.items():
        if counts >= 10:
            writer.write('{} {}\n'.format(key, counts))
