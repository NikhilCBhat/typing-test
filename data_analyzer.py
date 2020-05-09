class Analyzer:
    
    def __init__(self, word_results):
        self.data = word_results
    
    def generate_stats(self):
        total_characters = sum([len(x[1]) for x in self.data if x[0]])
        total_correct_words = len([x for x in self.data if x[0]])
        total_words = len(self.data)

        return {
            "WPM (adjusted)": round(total_characters/5, 2),
            "WPM (raw)": total_correct_words,
            "Accuracy": "{}%".format(round(100*total_correct_words/total_words, 2)),
            "Typed Words": total_words,
            "Correct Words": total_correct_words
        }