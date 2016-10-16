import twitter
from Tweet import Tweet
import sqlite3
import csv
import json
import urllib.request
import boto3


def createQuery(file):
    query = 'q='
    first_line = file.readline().replace('#', '%23').strip('\n')
    query += first_line
    for hashtag in file:
        query += '%2C%20OR%20' + hashtag.replace('#', '%23').strip('\n')
    query += '&src=typd&count=100'
    return query


def getTweets(query, party):
    results = api.GetSearch(raw_query=query)
    for result in results:
        if result.place is not None:
            bounding_box = result.place.get('bounding_box').get('coordinates')[0]
            tweet = Tweet((bounding_box[0][0] + bounding_box[1][0]) / 2, (bounding_box[1][1] + bounding_box[2][1]) / 2,
                          party, result.created_at)
            tweets.append(tweet)
        if (result.user.geo_enabled is True) and (len(result.user.location) > 0):
            print(result.user.location)
            if mydict.get(result.user.location.upper(), "Not Found") != "Not Found":
                response = urllib.request.urlopen("http://api.zippopotam.us/us/" + mydict[result.user.location.upper()]).read().decode('utf-8')
                data = json.loads(response)
                tweet = Tweet(data.get('places')[0].get('latitude'), data.get('places')[0].get('longitude'), party, result.created_at)
                tweets.append(tweet)


api = twitter.Api(consumer_key='rnBTENQ1GCJdZLVEuZheV6YJ6',
                  consumer_secret='b9g5TgNIXRKN7lwQxh5YcLk8AI59zQK3zzIAtAorspMHpUha3F',
                  access_token_key='787504691949076481-jwZbK3F3lc5evdzeExZO0DRj4LvWB1m',
                  access_token_secret='Q8DGppRwEFKWo5ZxbAjXCQUGAqBgCMU0t4ZI21RGoND3T')

republican_file = open('republican_hashtags.txt', 'r')
democrat_file = open('democrat_hashtags.txt', 'r')
# q=%23Trump%2C%20OR%20%23Hillary%2C%20OR%20%23Kane&count=100
republican_query = createQuery(republican_file)
democrat_query = createQuery(democrat_file)

with open('Zipcodes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[3] + ", " + rows[4]: rows[1] for rows in reader}

tweets = []
getTweets(republican_query, 'Republican')
getTweets(democrat_query, 'Democrat')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tweets')
id = 1
for tweet in tweets:
    response = table.put_item(
        Item={
            'id' = id,
            'lat' = tweet.latitude,
            'long' = tweet.longitude,
            'party' = tweet.party,
            'time' = tweet.timestamp
        }
    )
    id += 1
