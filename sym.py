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
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)
# sym_spell.load_dictionary("dictionary/cities.txt", term_index=0, count_index=1)
# sym_spell.load_dictionary("dictionary/names.txt", term_index=0, count_index=1)
# sym_spell.load_dictionary("data/places.txt", term_index=0, count_index=1)
# sym_spell.load_bigram_dictionary("dictionary/bigram.txt", term_index=0, count_index=2)

# lookup suggestions for multi-word input strings (supports compound
# splitting & merging)
input_term = (
    # "austinlivermore texas"
    # "When was Ingrid corm"
    "sodium attraction dorce"
    # "artfactory"
    # "lightshow"
    # "Keller Memorial Hospital in Scranton, Pennsylvania"
)
# max edit distance per lookup (per single word, not per whole input string)
suggestions = sym_spell.lookup_compound(sym_spell.word_segmentation("austinlivermore texas").corrected_string, max_edit_distance=2)
# print(sym_spell.word_segmentation("austinlivermore texas").corrected_string)
# print(sym_spell.word_segmentation("artfactory").corrected_string)

# display suggestion term, edit distance, and term frequency
for suggestion in suggestions:
    print(suggestion.term, suggestion.distance, suggestion.count, "\n")

print(len(sym_spell.replaced_words))
