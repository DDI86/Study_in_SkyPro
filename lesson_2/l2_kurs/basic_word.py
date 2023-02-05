class BasicWord:

    def __init__(self, full_word, sub_words):
        self.full_word = full_word
        self.sub_words = sub_words

    def get_word_capitalised(self):
        return self.full_word.upper()

    def has_subwords(self, word):
        return word in self.sub_words

    def get_subwords_count(self):
        return len(self.sub_words)
