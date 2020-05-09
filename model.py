class TypingModel:

    def __init__(self, words):
        """
        Initializes a model. 
        At minimum, a model needs a collection of words.
        """
        self.words = words
    
    def process_input(self, user_word):
        """
        Processes the user's input.
        Should return a boolean indicating 
        whether the input is correct or false.
        """
        return
    
    def get_current_words(self):
        """
        Returns both the currect active word, 
        and the other words the user needs to type.
        """
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
