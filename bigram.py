from collections import Counter
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
from gensim.models.phrases import Phrases, ENGLISH_CONNECTOR_WORDS

nlp = English()
tokenizer = Tokenizer(nlp.vocab)

sentences = []
bigram = Phrases()
with open("corpus.txt", "r") as ifile:
    for line in ifile:
        sentence = [word.text for word in tokenizer(line.strip())]
        sentences.append(sentence)
        bigram.add_vocab([sentence])


bigram_model = Phrases(sentences, min_count=2, threshold=2, connector_words=ENGLISH_CONNECTOR_WORDS, delimiter=" ")
bigram_model_counter = Counter()
for key in bigram_model.vocab.keys():
    if len(key.split(" ")) > 1:
        bigram_model_counter[key] += bigram_model.vocab[key]

for key, counts in bigram_model_counter.most_common(50):
    print('{} {}'.format(key, counts))
