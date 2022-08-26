import pkg_resources
import spacy
from symspellpy import SymSpell

nlp = spacy.load("en_core_web_sm", exclude=["parser"])
nlp.enable_pipe("senter")

sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
bigram_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_bigramdictionary_en_243_342.txt"
)
# term_index is the column of the term and count_index is the
# column of the term frequency
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_dictionary("dictionary/cities.txt", term_index=0, count_index=2)
sym_spell.load_dictionary("dictionary/names.txt", term_index=0, count_index=2)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)
