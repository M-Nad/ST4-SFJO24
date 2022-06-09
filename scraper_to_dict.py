import re
from scrap_to_db import to_db

# tweet = r"{'id': 1533327171355299841, 'date': '2022-06-05 05:57:40', 'text': \"Future history lesson: PM Boris Johnson pictured at Queen Elizabeth's Platinum Jubilee celebrations prior to this highly unpopular PM forced resignation. Johnson was loudly booed the previous day by a crowd watching dignitaries arrive at St Paul's.  #JohnsonOut131 #JohnsonOut\", 'nombre_likes': 2, 'nombre_retweets': 1}"

def text_to_dict(file):
    pattern = r'(?:{\'id\': )|(?:, \'date\': \')|(?:\', \'text\': \'?\\?\"?)|(?:\'?\\?\"?, \'nombre_likes\': )|(?:, \'nombre_retweets\': )|(?:}\\?n?)'
    content = ""
    with open (file,"r") as f:
        content = f.read()
        f.close()

    ls_raw = re.split(pattern,content)

    ls_dict = []
    tweet_dict = {}
    for elem in ls_raw:
        if len(elem) > 0:
            # print(elem)
            if "id" not in tweet_dict:
                tweet_dict["id"] = int(elem)
            elif "date" not in tweet_dict:
                tweet_dict["date"] = '"'+elem+'"'
            elif "text" not in tweet_dict:
                text = re.sub('@',"",elem)
                text = re.sub('#',"",text)
                tweet_dict["text"] = text
            elif "nb_likes" not in tweet_dict:
                tweet_dict["nb_likes"] = int(elem)
            elif "nb_rt" not in tweet_dict:
                tweet_dict["nb_rt"] = int(elem)
                ls_dict += [tweet_dict]
                tweet_dict = {}
    # return list_dict
    to_db(ls_dict)


        
