class Player:

    def __init__(self, name):
        self.name = name
        self.words_used = []

    def get_name(self):
        return self.name

    def get_used_words_count(self):
        return len(self.words_used)

    def is_word_used(self, word):
        return word in self.words_used

    def add_word(self, word):
        self.words_used.append(word)
