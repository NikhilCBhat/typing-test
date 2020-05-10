import random

def document_to_words(filepath, shuffle=False):
    with open(filepath) as f:
        s = f.read()

    words = [x for x in s.split('\n') if all([96 < ord(c.lower()) < 124 for c in x ]) and x]
    if shuffle:
        random.shuffle(words)
    return words