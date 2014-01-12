import requests
import requests_oauthlib
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
import PMRkeys #PMRkeys is a separate local .py file with the Twitter Application Oauth credentials listed (not here for obvious reasons!) 
import json # will be needed to handle json

# ---------- define variables
adminURL='https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdGp1NmxJVXVHcGhIel9CNUxJUk8yYXc&output=csv'
#  ----------- end -------------

# ------------- search twitter as a function ---------------
def search_tweets (term,t_type,count) : # params: term= 'what to search for' type = 'how to search' Count = 'number of tweets' (max 100)    search_url_root='https://api.twitter.com/1.1/search/tweets.json?q='
    # check what type the search term is
    search_url_root='https://api.twitter.com/1.1/search/tweets.json?q='
    if t_type=='username':
        print ('searching twitter API for term: @'+term)
        term='%40'+term # add unicode for @ sign (%40) if a username search term
    else:
        if t_type=='hashtag':
            print ('searching twitter API for term: #'+term)
            term='%23'+term # add unicode for # sign (%40) if a hashtag search term
        else:
            print ('searching for term: '+term) # or just search!
    search_url=str(search_url_root+term+'&count='+count)
    print ('---------------------------')
    print ()
    auth = OAuth1(PMRkeys.PMR_consumer_key, PMRkeys.PMR_consumer_secret,PMRkeys.PMR_access_token,PMRkeys.PMR_access_secret )
    auth_response=requests.get(search_url, auth=auth)
    # print ('auth_response.text') # - uncomment to check the text is returning as expected
    # print (auth_response.text) # - uncomment to check the text is returning as expected
    j = (auth_response.text)
    js = json.loads(j)
    c = int(count)
    x=0
    while (x<c):
        print ('---------------')
        tweet_id = js['statuses'][x]['id']
        print ('Tweet '+str(x+1)+' of '+str(c)+'. Tweet id: '+str(tweet_id))
        name = js['statuses'][x]['user']['name']
        user = js['statuses'][x]['user']['screen_name']
        username= '@'+user
        print ('From:'+username+'('+name+')')
        tweet = js['statuses'][x]['text']
        # print ('print js: ')
        # print (js)
        print (tweet)
        x=x+1
    print ('---------------')  
    
# ------------- end search twitter -------------------------

# ------------- retrieve any google spreadsheet as data ----
def retrieveArray (url):
    stopWords = []
    Ws= requests.get(url)
    yy= Ws.text
    stopwords = yy.splitlines()

    print ('stopwords ------------')
    print (stopwords)
    print ('--------')

    print ('full list returned raw with line breaks --------')
    print (yy)
    print ('stopwords --------')
    print (stopwords)
    print ('--------')
    swCount=0
    for count in stopwords:
        swCount+=1
    print ('count  -----')
    print ('count = '+str(swCount))
    # end retrieveArray
    
# ------------- end retrieve data ---------------------------
search_tweets('musetech','hashtag','15')
retrieveArray(adminURL)
