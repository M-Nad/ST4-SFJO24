import re
from scrap_to_db import to_db

# tweet = r"{'id': 1533327171355299841, 'date': '2022-06-05 05:57:40', 'text': \"Future history lesson: PM Boris Johnson pictured at Queen Elizabeth's Platinum Jubilee celebrations prior to this highly unpopular PM forced resignation. Johnson was loudly booed the previous day by a crowd watching dignitaries arrive at St Paul's.  #JohnsonOut131 #JohnsonOut\", 'nombre_likes': 2, 'nombre_retweets': 1}"

def text_to_dict(file):
    pattern = r'(?:{\'id\': )|(?:, \'date\': \')|(?:\', \'text\': \'?\\?\"?)|(?:\'?\\?\"?, \'nombre_likes\': )|(?:, \'nombre_ret? ?tweets\': )|(?:}\\?n?)'
    content = ""
    ls_raw = []
    with open (file,"r",encoding="utf8") as f:
        content = f.readlines()
        f.close()

    ls_concatenate = []
    for raw in content:
        if raw[0]!="{":
            while len(ls_concatenate[-1])>2 and ls_concatenate[-1][-2:]=="\n":
                if ls_concatenate[-1][-3:]=="\\n":
                    ls_concatenate[-1]=ls_concatenate[-1][:-3]
                else:
                    ls_concatenate[-1]=ls_concatenate[-1][:-2]

            if  ls_concatenate[-1][-1]==",":
                print(ls_concatenate[-1])
                ls_concatenate[-1]=ls_concatenate[-1]+" "+raw
            else:
                ls_concatenate[-1]=ls_concatenate[-1]+raw
        else:
            ls_concatenate.append(raw)

    ls_raw = []
    for line in ls_concatenate:
        ls_raw+=re.split(pattern,line)

    ls_dict = []
    tweet_dict = {}
    for elem in ls_raw:
        space = re.findall("\s*\n",elem)
        if len(elem) > 0 and (len(space) == 0 or len(space[0]) < len(elem) ):
            if "id" not in tweet_dict:
                tweet_dict["id"] = int(elem)
            elif "date" not in tweet_dict:
                tweet_dict["date"] = '"'+elem+'"'
            elif "text" not in tweet_dict:
                text = re.sub('@',"",elem)
                text = re.sub('#',"",text)
                text = text.replace('"',"''")
                text = text.replace("'","''")
                tweet_dict["text"] = text
            elif "nb_likes" not in tweet_dict:
                tweet_dict["nb_likes"] = int(elem)
            elif "nb_rt" not in tweet_dict:
                tweet_dict["nb_rt"] = int(elem)
                print(tweet_dict)
                ls_dict.append(tweet_dict)
                tweet_dict = {}
    to_db(ls_dict)