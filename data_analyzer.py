import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analyzer:
    
    def __init__(self, word_results):
        self.data = pd.DataFrame(word_results, columns=["Status", "Word", "UserInput", "Time"])
        self.data.to_csv("data.csv")
        print(self.data)
    
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
    
    def generate_bar_graph(self):
        sns.set(style="whitegrid")
        sns.barplot(x="Word", y="Time", data=self.data)
        plt.show()


if __name__ == "__main__":
    data = [
        [True, "dog", "dog", 1],
        [True, "cat", "cat", 3]
        ]
    a = Analyzer(data)
    a.generate_bar_graph()