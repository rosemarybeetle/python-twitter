import httplib2
import requests
import requests_oauthlib
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
import PMRkeys
import json


# -------------- test output ------------
print ('test print keys for checking correct import')
print ("PMR_consumer_key = "+PMRkeys.PMR_consumer_key)
print ("PMR_consumer_secret = "+PMRkeys.PMR_consumer_secret)
print ("PMR_access_token = " + PMRkeys.PMR_access_token)
print ("PMR_access_secret = "+PMRkeys.PMR_access_secret)
# -------------- end test ---------------

# set search url for twitter
search_url = 'https://api.twitter.com/1.1/search/tweets.json?q=%40museweb'
auth = OAuth1(PMRkeys.PMR_consumer_key, PMRkeys.PMR_consumer_secret,PMRkeys.PMR_access_token,PMRkeys.PMR_access_secret )
auth_response=requests.get(search_url, auth=auth)
print ('auth_response.text')
print (auth_response.text)
print ('---------------')
print ('auth_response.json()')
auth_json = auth_response.json()
print (auth_json)
print ('---------------')
