from util import document_to_words
from controller import BasicTypingController
from model import SimpleModel
from view import BasicTypingView, QtView
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run typing test script")
    parser.add_argument('-d', action='store_true', help="Run in debug mode with simple command-line frontend")
    parser.add_argument('-t', '--time', type=int, help="Time to run test for", default=60)
    args = parser.parse_args()

    v = BasicTypingView() if args.d else QtView()

    w = document_to_words("file.txt", shuffle=True)
    m = SimpleModel(w)
    c = BasicTypingController(v, m, args.time)

    c.run()
