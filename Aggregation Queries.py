from pymongo import MongoClient 
client = MongoClient('localhost:27017')
db = client.twitter
#importing the database twitter as db via the client at 27017

def most_tweets():
    result = db.tweets.aggregate([{"$group" : {"_id" : "$user.screen_name", "count" : {"$sum" : 1}}}, 
                                  {"$sort" : {"count" : -1}}])
    return result
#to gather the twitter users in order of number of tweets
    
def highest_ratio():
    result = db.tweets.aggregate([{"$match" : {"user.friends_count" : {"$gt": 0},"user.followers_count" : {"$gt": 0}}},
                                {"$project" : {"ratio" : {"$divide" : ["$user.followers_count", "$user.friends_count"]},  
                                               "screen_name" : "$user.screen_name"}},
                                {"$sort" : {"ratio" : -1 }},
                                {"$limit" : 1}])
    return result
#to find the user who has the highest followers to followees ratio
    
def popular_specific():
    result = db.tweets.aggregate([{"$match": {"user.time_zone" : "Brasilia", "user.statuses_count" : {"$gte" : 100}}},
                                   {"$project" : {"_id" : "$_id",
                                                   "followers" : "$user.followers_count",
                                                   "screen_name" : "$user.screen_name",
                                                   "tweets" : "$user.statuses_count"}},
                                    {"$sort" : {"followers" : -1}},
                                    {"$limit" : 1}])
    return result
#here we are interested in the most popular user of a specific time zone
    
def specific_count():
    result = db.cities.aggregate([{"$match" : { "country" : "India"}},
                                  {"$unwind" : "$isPartOf"},
                                  {"$group" : {"_id" : "$isPartOf", "count" : {"$sum" : 1}}},
                                  {"$sort" : {"count" : -1}},
                                  {"$limit" : 1}])
    return result
#to know the district or region of a specific state with the most cities (using the cities database)

def most_avg_retweets():
    result = db.tweets.aggregate([{"$unwind" : "$entities.hashtags"},
                                  {"$group" : {"_id" : "$entities.hashtags.text", "retweets_avg" : {"$avg" : "$retweets_count"}}},
                                  {"$sort" : {"retweets_avg" : -1}}])
    return result
#returning the tweet most retweeted on average based on the hashtag
    
def unique_hashtags_by_user():
    result = db.tweets.aggregate([{"$unwind" : "$entities.hastags"},
                                  {"$group" : {"_id" : "$user.screen_name", "unique_hashtags" : 
                                                              {"$addToSet" : "$entities.hashtags.text"}}},
                                  {"$sort" : {"_id" : -1}}])
    return result
#if we were interested in the user who used most unique hashtags in singular tweets
    
def user_tweets_count():
    result = db.tweets.aggregate([{"$match": {"user.statuses_count": {"$gte": 0}}},
                                  {"$group": {"_id": "$user.screen_name","count": {"$sum": 1}, "tweet_texts": {"$push": "$text"}}},
                                  {"$sort": {"count": -1}},
                                  {"$limit": 5}])
    return result
#to return the top5 users by number of tweets