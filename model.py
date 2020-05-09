class TypingModel:

    def __init__(self, words):
        self.words = words


class SimpleModel(TypingModel):

    def __init__(self, words=["dog", "cat"]):
        super().__init__(words)
        self._next_word()
    
    def process_input(self, user_word):
        correct_input = user_word == self.active_word
        self._next_word()
        return correct_input
    
    def _next_word(self):
        if self.words:
            self.active_word = self.words.pop()
        else:
            self.active_word = None
    
    def get_current_word(self):
        return self.active_word
