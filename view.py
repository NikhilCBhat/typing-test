from PyQt5.QtWidgets import QApplication, QLabel


class TypingView:
    def __init__(self):
        return

    def show_words(self, words_to_show):
        return

    def recieve_input(self):
        return


class QtView(TypingView):
    def __init__(self):
        super().__init__()

        self.app = QApplication([])
        label = QLabel("Hello World")
        label.show()
        self.app.exec_()
