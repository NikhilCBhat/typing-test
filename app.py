from controller import BasicTypingController
from model import SimpleModel
from view import BasicTypingView, QtView

if __name__ == "__main__":
    m = SimpleModel(["dog", "cat", "apple", "banana", "lorem"])
    v = QtView()
    c = BasicTypingController(v, m)

    c.start()
