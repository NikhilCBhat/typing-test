import time

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
        self.start_time = time.time()
        self.previous_end_time = time.time()

        self.view.start_view()

    def process_input(self, word):
        ## Gets status from the model
        status = self.model.process_input(word, time.time()-self.previous_end_time)
        self.previous_end_time = time.time()
        
        ## View shows the status
        self.view.show_user_result(status)

        ## Check End State, If necessary end the game
        current_word, next_words = self.model.get_current_words()
        if current_word is None or time.time() - self.start_time < 60:
            self.view.end_game(self.model.get_results())

        ## Shows the words on the view
        self.view.show_words(current_word, next_words)


    def start(self):
        self.start_time = time.time()
        # current_word, next_words = self.model.get_current_words()
        # while current_word and time.time()-self.start < 60:
        #     self.view.show_words(current_word, next_words)
        #     self.view.recieve_input()
        #     current_word, next_words = self.model.get_current_words()

        # self.view.end_game(self.model.get_results())
