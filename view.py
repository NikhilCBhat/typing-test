import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import QRect

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
        self.started = False
        self.app = QApplication([])

    def show_words(self, active_word, other_words):

        self.labelActiveWord.setText(active_word)
        self.labelOtherWords.setText(' '.join(other_words[:10]))

    def show_user_result(self, correct_word):
        # TODO
        # Ideas 
        #   1) Another text label 
        #   2) Screen  flash a color
        return

    def start_view(self):
        self.window = QWidget()

        geometry = self.app.desktop().screenGeometry()
        x = 0.25 * geometry.width()
        y = 0.25 * geometry.height()
        w = 2 * x
        h = 2 * y
        geometry.setX(x)
        geometry.setY(y)
        geometry.setWidth(w)
        geometry.setHeight(h)

        self.window.setGeometry(geometry)
        self.window.setWindowTitle("Typing Test")

        ##########
        ## WIDGETS
        self.labelActiveWord = QLabel("Press the spacebar to begin")
        self.labelActiveWord.setStyleSheet("font: 18pt; color: Blue;")
        self.labelOtherWords = QLabel("")
        self.labelOtherWords.setStyleSheet("font: 18pt; color: Grey;")

        self.wordBox = QLineEdit()

        self.quitButton = QPushButton("QUIT")
        self.restartButton = QPushButton("RESTART")

        self.tableResults = QTableWidget()
        ##########

        mainLayout = self._build_layout()
        self.window.setLayout(mainLayout)
        
        ##########
        ## SIGNALS
        self.wordBox.textChanged.connect(self._handle_text_change)
        self.quitButton.clicked.connect(self._quit)
        ##########

        self.window.show()
        self.app.exec_()

    def _quit(self):
        print("Quitting")
        sys.exit()

    def end_game(self, results):
        self.labelActiveWord.hide()
        self.labelOtherWords.hide()
        self.wordBox.hide()
        self.tableResults.show()

        self.tableResults.setRowCount(len(results))

        for i, (k, v) in enumerate(results.items()):
            self.tableResults.setItem(i, 0, QTableWidgetItem(k))
            self.tableResults.setItem(i, 1, QTableWidgetItem(str(v)))

        return

    def _handle_text_change(self):
        if not self.started:
            self.started = True
            self.controller.start_game()
        else:
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

        buttons = QWidget()
        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.quitButton)
        btnLayout.addWidget(self.restartButton)
        buttons.setLayout(btnLayout)

        self.tableResults.setRowCount(2)
        self.tableResults.setColumnCount(2)

        layoutTop.addWidget(words)
        layoutTop.addWidget(self.wordBox)
        layoutTop.addWidget(self.tableResults)
        layoutTop.addWidget(buttons)
        self.tableResults.hide()

        return layoutTop

class BasicTypingView(TypingView):
    def __init__(self):
        super().__init__()
        self.started = False

    def show_words(self, active_word, other_words):
        print("Type: {}   Next: {}".format(active_word,
                                           ' '.join(other_words[:10])))

    def show_user_result(self, correct_word):
        print("{}\n".format("Good Job!" if correct_word else "Incorrect!"))

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

    def _recieve_input(self):
        """
        Gets input from the command line, and sends that to the controller.
        """
        user_word = input("Text: ").strip()
        self.controller.process_input(user_word)