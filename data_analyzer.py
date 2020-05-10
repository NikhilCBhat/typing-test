import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analyzer:

    def __init__(self, word_results, dataframe=False):
        if dataframe:
            self.data = word_results
        else:
            self.data = pd.DataFrame(word_results, columns=["Status", "Word", "UserInput", "Time"])

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
        sorted_data = self.data.sort_values(by=["Time"], ascending=False)
        sns.set(style="whitegrid")
        chart = sns.barplot(x="Word", y="Time", data=sorted_data)
        chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
        plt.show()


if __name__ == "__main__":
    data = pd.read_csv("data.csv")
    a = Analyzer(data, dataframe=True)
    a.generate_bar_graph()