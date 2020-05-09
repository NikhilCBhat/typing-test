class TypingView:

    def __init__(self):
        return

    def show_words(self, active_word, other_words):
        return

    def recieve_input(self):
        return

    def set_controller(self, controller):
        self.controller = controller

    def show_user_result(self, correct_word):
        return


class BasicTypingView(TypingView):

    def __init__(self):
        super().__init__()

    def show_words(self, active_word, other_words):
        print("Type: {}   Next: {}".format(
            active_word, ' '.join(other_words)
        ))

    def recieve_input(self):
        user_word = input("Text: ")
        self.controller.process_input(user_word)

    def show_user_result(self, correct_word):
        print("{}\n".format(
            "Good Job!" if correct_word else "What a Loser!"
        ))
