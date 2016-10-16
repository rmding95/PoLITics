import twitter

api = twitter.Api(consumer_key='rnBTENQ1GCJdZLVEuZheV6YJ6',
                  consumer_secret='b9g5TgNIXRKN7lwQxh5YcLk8AI59zQK3zzIAtAorspMHpUha3F',
                  access_token_key='787504691949076481-jwZbK3F3lc5evdzeExZO0DRj4LvWB1m',
                  access_token_secret='Q8DGppRwEFKWo5ZxbAjXCQUGAqBgCMU0t4ZI21RGoND3T')
hashtags = ['TrumpPence']
tweets = []
results = api.GetSearch(raw_query='f=tweets&vertical=default&q=%23TrumpPence&count=100')
for result in results:
    if (result.coordinates is not None) or (result.location is not None) or (result.place is not None) \
            or (result.geo is not None) or (result.user.geo_enabled is True):
        tweets.append(result)

print(tweets)
