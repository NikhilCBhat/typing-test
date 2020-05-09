class TypingModel:

    def __init__(self, words):
        """
        Initializes a model. 
        At minimum, a model needs a collection of words.
        """
        self.words = words

    def process_input(self, user_word, time_elapsed):
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
        self.results = []
        self.stats = {}

    def process_input(self, user_word, time_elapsed):
        active_word, _ = self.get_current_words()
        correct_input = user_word == active_word
        self.results.append((correct_input, active_word, user_word, time_elapsed))
        self._next_word()
        return correct_input

    def _next_word(self):
        self.active_word = self.words.pop() if self.words else None

    def get_current_words(self):
        return self.active_word, self.words[::-1]

    def get_results(self):
        self._generate_stats()
        return self.results, self.stats

    def _generate_stats(self):
        total_charectars = sum([len(x[1]) for x in self.results if x[0]])
        total_correct_words = len([x for x in self.results if x[0]])
        total_words = len(self.results)

        self.stats = {
            "WPM (adjusted)": round(total_charectars/5, 2),
            "WPM (raw)": total_correct_words,
            "Accuracy": "{}%".format(round(100*total_correct_words/total_words, 2)),
            "Typed Words": total_words,
            "Correct Words": total_correct_words
        }
