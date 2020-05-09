class TypingController:

    def __init__(self, view, model):
        self.view = view
        self.view.set_controller(self)
        self.model = model

    def process_input(self, word):
        status = self.model.process_input(word)
        next_word = self.model.active_word
        self.view.show_user_result(status)
        self.view.show_words(next_word)
    
    def start(self):
        current_word = self.model.get_current_word()
        while current_word:
            self.view.show_words(current_word)
            self.view.recieve_input()
            current_word = self.model.get_current_word()
        
        print("Game Completed!")
