# saveLastTweetId.py

def saveTweetId (tweetId):
    tweetIds = open('lastTweet.txt', 'w')
    tweetIds.write(tweetId)
    tweetIds.close()
