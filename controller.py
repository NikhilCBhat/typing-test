class TypingController:

    def __init__(self, view, model):
        """
        Initializes the controller with the view & model.
        """
        self.view = view
        self.view.set_controller(self)
        self.model = model

    def process_input(self, word):
        """
        Process the current input from the user. 
        Should have a callback to the model.
        """
        return
    
    def run(self):
        "Runs the program"
        return


class BasicTypingController(TypingController):

    def __init__(self, view, model):
        super().__init__(view, model)

    def process_input(self, word):
        status = self.model.process_input(word)
        self.view.show_user_result(status)

    def run(self):
        current_word, next_words = self.model.get_current_words()
        while current_word:
            self.view.show_words(current_word, next_words)
            self.view.recieve_input()
            current_word, next_words = self.model.get_current_words()

        self.view.end_game()
