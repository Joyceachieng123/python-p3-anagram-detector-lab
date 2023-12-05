# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        word_sorted = sorted(self.word)
        return [w for w in words if self.is_anagram(w, word_sorted)]

    def is_anagram(self, word, sorted_word):
        word = word.lower()
        if word == self.word:
            return False
        return sorted(word) == sorted_word
