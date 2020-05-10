from util import document_to_words
from controller import BasicTypingController
from model import SimpleModel
from view import BasicTypingView, QtView
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run typing test script")
    parser.add_argument('-d', action='store_true', help="Run in debug mode with simple command-line frontend")
    args = parser.parse_args()

  
    if args.d:
        v = BasicTypingView()
    else:
        v = QtView()

    w = document_to_words("file.txt", shuffle=True)
    m = SimpleModel(w)
    c = BasicTypingController(v, m)

    c.run()
