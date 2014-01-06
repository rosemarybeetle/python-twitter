import requests
import requests_oauthlib
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session

import PMRkeys #PMRkeys is a separate .py file with the Twitter Application Oauth credentials listed (not here for obvious reasons!) 
import json # will be needed to handle json


# -------------- test output of twitter authorisation codes from external .py file ------------
print ('test print keys for checking correct import')
print ("PMR_consumer_key = "+PMRkeys.PMR_consumer_key)
print ("PMR_consumer_secret = "+PMRkeys.PMR_consumer_secret)
print ("PMR_access_token = " + PMRkeys.PMR_access_token)
print ("PMR_access_secret = "+PMRkeys.PMR_access_secret)
# -------------- end test ---------------
'''
# set search url for twitter
# based on python library 'requests' - documentation here: http://docs.python-requests.org/en/latest/user/authentication/
search_url = 'https://api.twitter.com/1.1/search/tweets.json?q=%40museweb'
auth = OAuth1(PMRkeys.PMR_consumer_key, PMRkeys.PMR_consumer_secret,PMRkeys.PMR_access_token,PMRkeys.PMR_access_secret )
auth_response=requests.get(search_url, auth=auth)
print ('auth_response.text')
print (auth_response.text)
print ('---------------')
# get as json. See documentation here: http://docs.python-requests.org/en/latest/user/quickstart/
print ('auth_response.json()')
auth_json = auth_response.json()
print (auth_json)
print ('---------------')
'''

# ------------- search twitter as a function ---------------
def search_tweets (term,t_type,count) : # params - term=what to search for. type is how to search. Count = number of tweets (max 100)
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
    print ('auth_response.text')
    print (auth_response.text)
    print ('---------------')
    # get as json. See documentation here: http://docs.python-requests.org/en/latest/user/quickstart/
    print ('auth_response.json()')
    auth_json = auth_response.json()
    print (auth_json)
    print ('---------------')
# ------------- end search twitter -------------------------
search_tweets('museweb','username','2') 
