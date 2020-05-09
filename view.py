import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout


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

    def end_game(self, results):
        """
        Process the end of the game
        """
        return

    def start_view(self):
        """
        Starts the game
        """
        return


class QtView(TypingView):
    def __init__(self):
        super().__init__()

        self.app = QApplication([])

    def show_words(self, active_word, other_words):
        

        self.labelActiveWord.setText(active_word)
        self.labelOtherWords.setText(' '.join(other_words[:10]))

    def show_user_result(self, correct_word):
        # TODO
        # Lucas' creative decision here
        # IDeas: 1) Another text label 2) screen  flash a color 3) Emails your mom that you're bad @ typing if you make mistakes
        return

    def start_view(self):
        window = QWidget()
        window.setGeometry(10,10,300,200)
        window.setWindowTitle("Typing Test")
        
        ## WIDGETS
        self.labelActiveWord = QLabel("Press the spacebar to begin")
        self.labelActiveWord.setStyleSheet("font: 18pt; color: Blue;")
        self.labelOtherWords = QLabel("")
        self.labelOtherWords.setStyleSheet("font: 18pt; color: Grey;")

        self.wordBox = QLineEdit()

        self.wordBox.textChanged.connect(self._handle_text_change)
        ###

        mainLayout = self._build_layout()
        window.setLayout(mainLayout)
        
        window.show()
        self.app.exec_()

    def end_game(self, results):
        sys.exit()
        return

    def _handle_text_change(self):
        current_text = self.wordBox.text()
        if current_text and current_text[-1] == " ":
            self.controller.process_input(current_text.strip())
            self.wordBox.clear()

    def _build_layout(self):
        
        layoutTop = QVBoxLayout()
        
        words = QWidget()
        wordsLayout = QHBoxLayout()
        wordsLayout.addWidget(self.labelActiveWord)
        wordsLayout.addWidget(self.labelOtherWords)
        wordsLayout.setStretch(0, 0)
        wordsLayout.setStretch(1, 1)
        words.setLayout(wordsLayout)


        layoutTop.addWidget(words)
        layoutTop.addWidget(self.wordBox)

        return layoutTop

class BasicTypingView(TypingView):
    def __init__(self):
        super().__init__()
        self.started = False

    def show_words(self, active_word, other_words):
        print("Type: {}   Next: {}".format(active_word,
                                           ' '.join(other_words[:10])))

    def _recieve_input(self):
        user_word = input("Text: ").strip()
        self.controller.process_input(user_word)

    def show_user_result(self, correct_word):
        print("{}\n".format("Good Job!" if correct_word else "What a Loser!"))

    def end_game(self, results):
        print("Game Over!\nStats")

        for key, value in results.items():
            print(key, value)

        sys.exit()

    def start_view(self):
        input("Press Enter to begin!")
        self.controller.start_game()
        while True:
            self._recieve_input()
