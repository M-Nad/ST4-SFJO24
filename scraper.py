import twitter_connection_setup

api = twitter_connection_setup.twitter_setup()

def scrapping(query, date1, date2):

    #Nombre de tweets récupérés
    number_of_tweets = 1

    #Récupération des tweets
    tweets = api.search_tweets(q = query, lang = "fr", count = number_of_tweets, tweet_mode="extended")
    liste_tweet = []
    for tweet in tweets:
        info = {}
        info["id"] = tweet._json["id"]
        info["date"] = tweet._json["created_at"]
        info["text"] = tweet._json["full_text"] 
        liste_tweet.append(info)
        print(info)
    return liste_tweet
scrapping("sport", "2022-06-01", "2022-06-02")
