import requests
import requests_oauthlib
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
import PMRkeys #PMRkeys is a separate local .py file with the Twitter Application Oauth credentials listed (not here for obvious reasons!) 
import json # will be needed to handle json

# ---------- define variables
adminURL='https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdGp1NmxJVXVHcGhIel9CNUxJUk8yYXc&output=csv'
stopwordsURL ='https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdEJGSWJNRXJJQVc5ZVo2cHNGRFJ3WVE&output=csv'
searchTerm=""
searchType=""
tweetNum=""
harvestPeriod=""
introText=""
text2=""

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

# ------------- get admin settings--------------------------
def loadAdmin (url):
    retrieveArray(adminURL)
    
    st=results[0] # get search term
    aa=st.split(',')
    global searchTerm
    searchTerm =aa[1]
    
    stype=results[1] # get search term
    bb=stype.split(',')
    global searchType
    searchType =bb[1]
    
    tNum=results[2] # get search term
    cc=tNum.split(',')
    global tweetNum
    tweetNum =cc[1]

    hPeriod=results[3] # get search term
    dd=hPeriod.split(',')
    global harvestPeriod
    harvestPeriod =dd[1]
    
    iText=results[4] # get search term
    ee=iText.split(',')
    global introText
    introText =ee[1]
    
    t2=results[5] # get search term
    ff=t2.split(',')
    global text2
    text2 =ff[1]

   
    
# ----------------------------------------------------------

# ------------- retrieve any google spreadsheet as data ----
def retrieveArray (url):
    Ws= requests.get(url)
    yy= Ws.text
    global results
    results = yy.splitlines()

    print ('stopwords ------------')
    print (results)
    print ('--------')

    print ('full list returned raw with line breaks --------')
    print (yy)
    print ('stopwords --------')
    print (results)
    print ('--------')
    swCount=0
    for count in results:
        swCount+=1
    print ('count  -----')
    print ('count = '+str(swCount))
    # end retrieveArray
    
# ------------- end retrieve data ---------------------------

loadAdmin (adminURL)
retrieveArray(stopwordsURL)
search_tweets(searchTerm,searchType,tweetNum)
print ('-------99999999  end   9999-------')
print ('searchTerm = ')
print (searchTerm)
print ('searchType = ')
print (searchType)
print ('tweetNum')
print (tweetNum)
print ('harvestPeriod')
print (harvestPeriod)
print ('introText')
print (introText)
print ('text2')
print (text2)


print ('---- stopwords ------------')


