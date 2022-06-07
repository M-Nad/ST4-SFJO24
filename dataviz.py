import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import scrap_to_db as STDB


# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")

db = STDB.db_to_dataframe()

def chart_bar(db):
    dict_chart = {"date":[],"score":[],"count":[]}
    dict_count = db.groupby(["date","score"]).count().to_dict()["tweet_id"]
    for key in dict_count:
        dict_chart["date"].append(key[0])
        dict_chart["score"].append(key[1])
        dict_chart["count"].append(dict_count[key])
    chart_dataframe = pd.DataFrame(dict_chart)
    sns.catplot(data=chart_dataframe, x="date", y="count", hue="score", kind = "bar")
    #return chart_dataframe

def chart_pie(data = [65,5,30]):
    labels = ['Positif', 'Neutre', 'Négatif']
    #define Seaborn color palette to use
    colors = [sns.color_palette('pastel')[2],sns.color_palette('pastel')[6],sns.color_palette('pastel')[3]]
    plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
    plt.show()

#sns.displot(data=x, x="date",y="tweet_id", hue="score")
#sns.catplot(data=x, x="date", y="Count", hue="score", kind = "bar")