class TypingModel:

    def __init__(self, words):
        self.words = words
    
    def process_input(self, user_word):
        return
    
    def get_current_words(self):
        return


class SimpleModel(TypingModel):

    def __init__(self, words):
        super().__init__(words)
        self._next_word()
    
    def process_input(self, user_word):
        correct_input = user_word == self.get_current_words()[0]
        self._next_word()
        return correct_input
    
    def _next_word(self):
        self.active_word = self.words.pop() if self.words else None

    def get_current_words(self):
        return self.active_word, self.words
