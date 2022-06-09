# -*- coding: utf-8 -*-
import twitter_connection_setup
import utils.scrap_to_db as STDB

api = twitter_connection_setup.twitter_setup()


def scrapping(query):

    # Nombre de tweets récupérés
    number_of_tweets = 50

    # Récupération des tweets
    tweets = api.search_tweets(q=query + " " + " " +
                               "-filter:retweets AND -filter:links", lang="en", count=number_of_tweets, tweet_mode="extended")
    liste_tweet = []
    for tweet in tweets:
        info = {}
        info["id"] = tweet._json["id"]
        date = '2022-06-' + \
            tweet._json["created_at"][8:10] + ' ' + \
            tweet._json["created_at"][11:19]
        info["date"] = date
        texte = tweet._json["full_text"]
        texte=texte.replace("'"," ")
        texte=texte.replace('"'," ")
        #texte.replace(" ' ", ' " ')
        texte = texte.strip('\n') 
        info["text"] = texte
        info["nombre_likes"] = tweet._json["favorite_count"]
        info["nombre_retweets"] = tweet._json["retweet_count"]
        liste_tweet.append(info)
        print(info) #afficher les tweets dans la console 
        STDB.to_db(liste_tweet)
    return liste_tweet


scrapping("#BackBoris")
