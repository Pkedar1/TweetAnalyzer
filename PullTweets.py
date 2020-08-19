import tweepy
import sys
#import threading
#import time

# Keys from Twitter Dev Console
consumer_key = "xxxxx"
consumer_secret = "xxxxx"
access_token = "xxxx"
access_token_secret = "xxxxx"
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
    def on_status(self, status):
        #searchTerms = ["coronavirus","Coronavirus","COVID-19","COVID"]
        #for term in searchTerms:
            #if status.text.find(term) >= 0:
        print(status.geo)
        print(status.text)
        if status.text.find("RT", 0, 4) == -1:
            csvFile.write(str(status.text.encode("utf-8")) + "\n")
            csvFile.flush()

    def on_error(self,status):
        print("Encountered error: " + status)
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