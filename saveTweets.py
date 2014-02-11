# saveTweets.py

def saveTweet (tw):
    tweets = open('tweetstore.txt', 'a')
    tweets.write(tw)
    tweets.write('\n')
    tweets.close()
