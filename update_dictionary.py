from symspellpy import SymSpell

sym_spell = SymSpell()
corpus_path = "corpus.txt"
sym_spell.create_dictionary(corpus_path)

print(sym_spell.words)
print(sym_spell.bigrams)