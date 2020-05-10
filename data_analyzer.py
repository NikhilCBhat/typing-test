import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analyzer:

    def __init__(self, word_results, dataframe=False, output_filename=None):
        if dataframe:
            self.data = word_results
        else:
            self.data = pd.DataFrame(word_results, columns=["Status", "Word", "User_Input", "Time"])
        
        if output_filename:
            self.data.to_csv(output_filename)

    def generate_stats(self):
        total_characters = sum([len(x) for i,x in enumerate(self.data["Word"]) if self.data["Status"][i]])
        total_correct_words = len([x for x in self.data["Status"] if x])
        total_words = len(self.data["Word"])

        return {
            "WPM (adjusted)": round(total_characters/5, 2),
            "WPM (raw)": total_correct_words,
            "Accuracy": "{}%".format(round(100*total_correct_words/total_words, 2)),
            "Typed Words": total_words,
            "Correct Words": total_correct_words
        }

    def generate_bar_graph(self):
        sns.set(style="whitegrid")
        chart = sns.barplot(x="Word", y="Time", data=self.data.sort_values(by=["Time"], ascending=False), 
            hue="Status", dodge=False)
        chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
        plt.show()

    def generate_scatter_plot_time(self):
        sns.set(style="whitegrid")
        chart = sns.scatterplot(x="Order", y="Time", data=self.data, hue="Status")
        chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
        plt.show()

    def generate_scatter_plot_time_elapsed(self):
        self.data["Time_Elapsed"] = self.data["Time"].cumsum()
        self.data["Order"] = [i for i in range(len(self.data["Status"]))]
        sns.set(style="whitegrid")
        chart = sns.scatterplot(x="Order", y="Time_Elapsed", data=self.data, hue="Status")
        chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
        plt.show()

if __name__ == "__main__":
    data = pd.read_csv("data_two.csv")
    a = Analyzer(data, dataframe=True)
    print(a.generate_stats())
    a.generate_scatter_plot_time_elapsed()
