class TypingController:

    def __init__(self, view, model):
        self.view = view
        self.view.set_controller(self)
        self.model = model

    def process_input(self, word):
        return
    
    def start(self):
        return


class BasicTypingController(TypingController):

    def __init__(self, view, model):
        self.view = view
        self.view.set_controller(self)
        self.model = model

    def process_input(self, word):
        status = self.model.process_input(word)
        self.view.show_user_result(status)

    def start(self):
        current_word, next_words = self.model.get_current_words()
        while current_word:
            self.view.show_words(current_word, next_words)
            self.view.recieve_input()
            current_word, next_words = self.model.get_current_words()

        print("Game Completed!")
