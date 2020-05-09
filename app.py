from util import document_to_words
from controller import BasicTypingController
from model import SimpleModel
from view import BasicTypingView

if __name__ == "__main__":
    m = SimpleModel(document_to_words("file.txt"))
    v = BasicTypingView()
    c = BasicTypingController(v, m)

    c.run()