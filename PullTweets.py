import tweepy
import sys
import json
#import threading
#import time

# Keys from Twitter Dev Console
consumer_key = "QobA0uHXSEzzKaCDdY6KkrYJs"
consumer_secret = "frtKiSfi71JUSxmPkR8aXzhvM7oUB62G7TmlZA0aFoylZpVL9A"
access_token = "798271300775112705-ZEgbi48y0ImeKKSxmoW4euzXRk0RqjO"
access_token_secret = "5Pqzq4t8ypTxzYg3AaTfvpM7vgOdViWwzbnzMQgIZiAwD"
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
    #def on_status(self, status):
        #searchTerms = ["coronavirus","Coronavirus","COVID-19","COVID"]
        #for term in searchTerms:
            #if status.text.find(term) >= 0:
        #print(status.text)
        #if status.text.find("RT", 0, 4) == -1:
          #  print(status.text)
          #  csvFile.write(str(status.text.encode("utf-8")) + "\n")
           # csvFile.flush()
    def on_data(self, raw_data):
        try:
            data = json.loads(raw_data)                      #decode the json object from twitter
            print(data['text'])
            if data['text'].find("RT", 0, 4) == -1 and (data['coordinates'] or data['geo']):           #collect geo-tagged tweet
                lat = str(data['coordinates']['coordinates'][1])
                lon = str(data['coordinates']['coordinates'][0])
                print('Lat: %s' % lat)
                print('Lon: %s \n' % lon)
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


#def flushfile():
    #while True:
        #csvFile.write("\n")
        #csvFile.flush()
        #time.sleep(30)



streamListener = StreamListener()
#thread = threading.Thread(target=flushfile, daemon=True)
#thread.start()
myStream = tweepy.Stream(auth = api.auth, listener=streamListener, tweet_mode = "extended")
#myStream.filter(follow = ['14499829', "15134240", "820452522494226433", "189868631", "40156330", "2426189960", "39416218", "75937326", "2353701600", "1094762324097822720", "28023025", "1236557193752657926", "224896427", "487673211", "704282873231237121", "394087611", "18831926"], languages=["en"])
myStream.filter(track=["COVID", "COVID-19", "coronavirus"], languages=["en"])
#myStream.filter(languages=["en"])