class TypingView:

    def __init__(self):
        return
    
    def show_words(self, words_to_show):
        return
    
    def recieve_input(self):
        return
    
    def set_controller(self, controller):
        self.controller = controller


class BasicTypingView(TypingView):

    def __init__(self):
        super().__init__()
    
    def show_words(self, word):
        print(word)
    
    def recieve_input(self):
        user_word = input("Text: ")
        self.controller.process_input(user_word)
    
    def show_user_result(self, correct_word):
        if correct_word:
            print("Good job!")
        else:
            print("What a loser!")
