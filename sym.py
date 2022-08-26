import pkg_resources

from symspellpy import SymSpell

sym_spell = SymSpell(max_dictionary_edit_distance=2)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
bigram_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_bigramdictionary_en_243_342.txt"
)

# term_index is the column of the term and count_index is the
# column of the term frequency
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_dictionary("dictionary/cities.txt", term_index=0, count_index=1)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)
# dictionary_path = "./data/frequency_dictionary.txt"
# bigram_path = "./data/frequency_bigramdictionary.txt"

# sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
# sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)
# lookup suggestions for multi-word input strings (supports compound
# splitting & merging)
input_term = (
    "austinlivermore texas"
    "When was Ingrid corm"
    "sodium attraction dorce"
    "Keller Memorial Hospital in Scranton, Pennsylvania"
)
# max edit distance per lookup (per single word, not per whole input string)
suggestions = sym_spell.lookup_compound(input_term, max_edit_distance=2)
# display suggestion term, edit distance, and term frequency
for suggestion in suggestions:
    print(suggestion.term, suggestion.distance, suggestion.count, "\n")

print(len(sym_spell.replaced_words))
