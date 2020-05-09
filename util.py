def document_to_words(filepath):
    with open(filepath) as f:
        s = f.read()

    return [x for x in s.split(' ') if all([96 < ord(c.lower()) < 124 for c in x ]) and x]