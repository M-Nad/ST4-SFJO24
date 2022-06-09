import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import utils.scrap_to_db as STDB


# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")

db = STDB.db_to_dataframe()
db_senti = STDB.db_to_dataframe_sentiwordnet()

def chart_bar_count(db):
    dict_chart = {"date":[],"Score":[],"Nombre de tweets":[]}
    dict_count = db.groupby(["date","score"]).count().to_dict()["tweet_id"]
    for key in dict_count:
        dict_chart["date"].append(key[0])
        dict_chart["Score"].append(key[1])
        dict_chart["Nombre de tweets"].append(dict_count[key])
    chart_dataframe = pd.DataFrame(dict_chart)
    fig = plt.figure()
    colors = [sns.color_palette()[i] for i in [3,7,2]]
    sns.catplot(data=chart_dataframe, x="date", y="Nombre de tweets", hue="Score", kind = "bar",palette=colors)
    plt.savefig('./chart/chart_bar_count_score.png')
    return chart_dataframe

def chart_bar_percent(db):
    D = db.groupby(["date"]).any()
    dates = [date for date in D.index]
    dict_chart = {"date":[],"Score":[],"count":[]}
    dict_percent = {"date":[],"Score":[],"Pourcentage":[]}
    req_df=db.groupby(["date","score"]).count()
    dates = [date for date in D.index]
    index = req_df.index
    for date in dates:
        for score in [-1,0,1]:
            if not (date,score) in index:
                req_df.loc[(date,score),:]=[0]
    dict_count = req_df.to_dict()["tweet_id"]
    for key in dict_count:
        dict_chart["date"].append(key[0])
        dict_chart["Score"].append(key[1])
        dict_chart["count"].append(dict_count[key])
    percent=[]
    date_prec = ""
    count = 0
    i=0
    values=[]
    sorted_req_df=req_df.sort_index()
    for k in sorted_req_df.index:
        if k[0]==date_prec:
            count+=sorted_req_df["tweet_id"][k]
            values.append([i,sorted_req_df["tweet_id"][k]])
        else:
            if count !=0:
                for p in values:
                    dict_percent["date"].append(sorted_req_df["tweet_id"].index[p[0]][0])
                    dict_percent["Score"].append(sorted_req_df["tweet_id"].index[p[0]][1])
                    dict_percent["Pourcentage"].append(100*p[1]/count)
            date_prec=k[0]
            values=[[i,sorted_req_df["tweet_id"][k]]]
            count = sorted_req_df["tweet_id"][k]
        i+=1
    if count !=0:
        for p in values:
            dict_percent["date"].append(sorted_req_df["tweet_id"].index[p[0]][0])
            dict_percent["Score"].append(sorted_req_df["tweet_id"].index[p[0]][1])
            dict_percent["Pourcentage"].append(100*p[1]/count)
    percent_df = pd.DataFrame(dict_percent)
    colors = [sns.color_palette('pastel')[i] for i in [3,7,2]]
    fig = plt.figure()
    sns.catplot(data=percent_df, x="date", y="Pourcentage", hue="Score", kind = "bar", palette=colors)
    plt.savefig('./chart/chart_bar_percent_score.png')
    return percent_df


def chart_bar_count_senti(db):
    dict_chart = {"date":[],"Score":[],"Nombre de tweets":[]}
    dict_count = db.groupby(["date","score_sentiwordnet"]).count().to_dict()["tweet_id"]
    for key in dict_count:
        dict_chart["date"].append(key[0])
        dict_chart["Score"].append(key[1])
        dict_chart["Nombre de tweets"].append(dict_count[key])
    chart_dataframe = pd.DataFrame(dict_chart)
    fig = plt.figure()
    colors = [sns.color_palette()[i] for i in [3,7,2]]
    sns.catplot(data=chart_dataframe, x="date", y="Nombre de tweets", hue="Score", kind = "bar",palette=colors)
    plt.savefig('./chart/chart_bar_count_score_senti.png')
    return chart_dataframe

def chart_bar_percent_senti(db):
    D = db.groupby(["date"]).any()
    dates = [date for date in D.index]
    dict_chart = {"date":[],"Score":[],"count":[]}
    dict_percent = {"date":[],"Score":[],"Pourcentage":[]}
    req_df=db.groupby(["date","score_sentiwordnet"]).count()
    dates = [date for date in D.index]
    index = req_df.index
    for date in dates:
        for score in [-1,0,1]:
            if not (date,score) in index:
                req_df.loc[(date,score),:]=[0]
    dict_count = req_df.to_dict()["tweet_id"]
    for key in dict_count:
        dict_chart["date"].append(key[0])
        dict_chart["Score"].append(key[1])
        dict_chart["count"].append(dict_count[key])
    percent=[]
    date_prec = ""
    count = 0
    i=0
    values=[]
    sorted_req_df=req_df.sort_index()
    for k in sorted_req_df.index:
        if k[0]==date_prec:
            count+=sorted_req_df["tweet_id"][k]
            values.append([i,sorted_req_df["tweet_id"][k]])
        else:
            if count !=0:
                for p in values:
                    dict_percent["date"].append(sorted_req_df["tweet_id"].index[p[0]][0])
                    dict_percent["Score"].append(sorted_req_df["tweet_id"].index[p[0]][1])
                    dict_percent["Pourcentage"].append(100*p[1]/count)
            date_prec=k[0]
            values=[[i,sorted_req_df["tweet_id"][k]]]
            count = sorted_req_df["tweet_id"][k]
        i+=1
    if count !=0:
        for p in values:
            dict_percent["date"].append(sorted_req_df["tweet_id"].index[p[0]][0])
            dict_percent["Score"].append(sorted_req_df["tweet_id"].index[p[0]][1])
            dict_percent["Pourcentage"].append(100*p[1]/count)
    percent_df = pd.DataFrame(dict_percent)
    colors = [sns.color_palette('pastel')[i] for i in [3,7,2]]
    fig = plt.figure()
    sns.catplot(data=percent_df, x="date", y="Pourcentage", hue="Score", kind = "bar", palette=colors)
    plt.savefig('./chart/chart_bar_percent_score_senti.png')
    return percent_df


def chart_pie(db):
    labels = ['Positif', 'Neutre', 'Négatif']
    count = db.groupby(["score"]).count().to_dict()["tweet_id"]
    neg = (count[-1] if -1 in count.keys() else 0)
    nul = (count[0] if 0 in count.keys() else 0)
    pos = (count[1] if 1 in count.keys() else 0)
    tot = neg+nul+pos
    if tot > 0:
        data = [100*pos/tot,100*nul/tot,100*neg/tot]
        #define Seaborn color palette to use
        colors = [sns.color_palette('pastel')[i] for i in [2,7,3]]
        fig = plt.figure()
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
        plt.show()
        plt.savefig('./chart/chart_pie_score.png')
        return data
    else:
        print("No scores")

def chart_pie_senti(db):
    labels = ['Positif', 'Neutre', 'Négatif']
    count = db.groupby(["score_sentiwordnet"]).count().to_dict()["tweet_id"]
    neg = (count[-1] if -1 in count.keys() else 0)
    nul = (count[0] if 0 in count.keys() else 0)
    pos = (count[1] if 1 in count.keys() else 0)
    tot = neg+nul+pos
    if tot > 0:
        data = [100*pos/tot,100*nul/tot,100*neg/tot]
        #define Seaborn color palette to use
        colors = [sns.color_palette('pastel')[i] for i in [2,7,3]]
        fig = plt.figure()
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
        plt.show()
        plt.savefig('./chart/chart_pie_score_senti.png')
        return data
    else:
        print("No scores")

C_count = chart_bar_count(db)
C_percent = chart_bar_percent(db)
Pie_percent = chart_pie(db)

C_count_senti = chart_bar_count_senti(db_senti)
C_percent_senti = chart_bar_percent_senti(db_senti)
Pie_percent_senti = chart_pie_senti(db_senti)

#sns.displot(data=x, x="date",y="tweet_id", hue="score")
#sns.catplot(data=x, x="date", y="Count", hue="score", kind = "bar")