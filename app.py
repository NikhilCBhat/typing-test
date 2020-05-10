from util import document_to_words
from controller import BasicTypingController
from model import SimpleModel
from view import BasicTypingView, QtView

if __name__ == "__main__":
    w = document_to_words("file.txt", shuffle=True)
    m = SimpleModel(w)
    v = BasicTypingView()
    c = BasicTypingController(v, m)

    c.run()
