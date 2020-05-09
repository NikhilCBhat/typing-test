from controller import TypingController
from model import SimpleModel
from view import BasicTypingView

if __name__ == "__main__":
    m = SimpleModel()
    v = BasicTypingView()
    c = TypingController(v, m)

    c.start()