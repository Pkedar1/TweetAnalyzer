import tweepy
import sys
import json

# Keys from Twitter Dev Console
consumer_key = "xxxx"
consumer_secret = "xxxx"
access_token = "xxxx"
access_token_secret = "xxxx"
try:
    # Creating authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    csvFile = open('tweeta.csv', 'a')

except:
    print("Authentication Failed")


#Intializing stream
class StreamListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        try:
            data = json.loads(raw_data)
            print(data['text'])
            if data['text'].find("RT", 0, 4) == -1 and (data['coordinates'] or data['geo']):
                lat = str(data['coordinates']['coordinates'][1])
                lon = str(data['coordinates']['coordinates'][0])
                csvFile.write(str(data['text'].encode("utf-8")) + "|" + lat + "|" + lon + "\n")
                csvFile.flush()
        except Exception as e:
            print(e)

    def on_error(self,status):
        print("Encountered error: " )
        csvFile.close()
        sys.exit

    def on_disconnect(self, notice):
        csvFile.close()

streamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=streamListener, tweet_mode = "extended")
#myStream.filter(follow = ['14499829', "15134240", "820452522494226433", "189868631", "40156330", "2426189960", "39416218", "75937326", "2353701600", "1094762324097822720", "28023025", "1236557193752657926", "224896427", "487673211", "704282873231237121", "394087611", "18831926"], languages=["en"])
myStream.filter(track=["COVID", "COVID-19", "coronavirus"], languages=["en"])