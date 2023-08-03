''' Given an array of strings (str), group the anagrams together. You can return the
answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.'''

from collections import defaultdict
def group_anagrams(strings):
    anagrams = defaultdict(list)

    for word in strings:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())

input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(input_strings)
print(result)
