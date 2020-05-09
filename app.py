from util import document_to_words
from controller import BasicTypingController
from model import SimpleModel
from view import BasicTypingView, QtView

if __name__ == "__main__":
    m = SimpleModel(document_to_words("file.txt"))
    v = QtView()
    c = BasicTypingController(v, m)

    c.run()
