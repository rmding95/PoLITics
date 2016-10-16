import twitter
import geocoder
from Tweet import Tweet

api = twitter.Api(consumer_key='rnBTENQ1GCJdZLVEuZheV6YJ6',
                  consumer_secret='b9g5TgNIXRKN7lwQxh5YcLk8AI59zQK3zzIAtAorspMHpUha3F',
                  access_token_key='787504691949076481-jwZbK3F3lc5evdzeExZO0DRj4LvWB1m',
                  access_token_secret='Q8DGppRwEFKWo5ZxbAjXCQUGAqBgCMU0t4ZI21RGoND3T')

republican_query = ''
democrat_query = ''
file = open('Hashtags.txt', 'r')
https://twitter.com/search?q=%23Trump%2C%20OR%20%23Hillary%2C%20OR%20%23Kane&src=typd&lang=en
#file is republican first then democrat, with empty line to separate
republican = True
republican_query = file.readline().strip('\n')
for line in file:
    if line == '\n':
        republican = False
    if republican:
        republican_query +=

tweets = []
results = api.GetSearch(raw_query='f=tweets&vertical=default&q=%23TrumpPence&count=100')
for result in results:
    if result.place is not None:
        bounding_box = result.place.get('bounding_box').get('coordinates')[0]
        tweet = Tweet((bounding_box[0][0] + bounding_box[1][0]) / 2, (bounding_box[1][1] + bounding_box[2][1]) / 2,
                      'party', result.created_at)
        tweets.append(tweet)
    if (result.user.geo_enabled is True) and (len(result.user.location) > 0):
        #coords = geocoder.google(result.user.location)
        #if coords:
        tweet = Tweet(1, 1, 'party', result.created_at)
        tweets.append(tweet)
print(tweets)
