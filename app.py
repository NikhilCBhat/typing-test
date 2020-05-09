from view import QtView
from controller import BasicTypingController
from model import SimpleModel
from view import BasicTypingView

if __name__ == "__main__":
    m = SimpleModel(["dog", "cat", "apple", "banana", "lorem"])
    v = BasicTypingView()
    c = BasicTypingController(v, m)

    c.start()
