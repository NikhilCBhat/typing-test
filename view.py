class TypingView:

    def __init__(self):
        """
        Initializes a view.
        """
        return

    def show_words(self, active_word, other_words):
        """
        Shows the user's active word, 
        and the other word they have yet to type.
        """
        return

    def recieve_input(self):
        """
        Recieves input from the user. 
        Should have a traceback to the controller's `process_input` function.
        """
        return

    def set_controller(self, controller):
        """
        Sets the controller for the view.
        """
        self.controller = controller

    def show_user_result(self, correct_word):
        """
        Lets the user know whether the word is correct.
        """
        return
    
    def end_game(self):
        """
        Process the end of the game
        """
        return


class BasicTypingView(TypingView):

    def __init__(self):
        super().__init__()

    def show_words(self, active_word, other_words):
        print("Type: {}   Next: {}".format(
            active_word, ' '.join(other_words[:10])
        ))

    def recieve_input(self):
        user_word = input("Text: ").strip()
        self.controller.process_input(user_word)

    def show_user_result(self, correct_word):
        print("{}\n".format(
            "Good Job!" if correct_word else "What a Loser!"
        ))

    def end_game(self, results):
        print("Game Over!")
        raw_results, num_words = results
        for r in raw_results:
            print(r)
        print("{} WPM".format(num_words))