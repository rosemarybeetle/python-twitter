import httplib2
import PMRkeys
print ("PMR_consumer_key = "+PMRkeys.PMR_consumer_key)
print ("PMR_consumer_secret = "+PMRkeys.PMR_consumer_secret)
print ("PMR_access_token = " + PMRkeys.PMR_access_token)
print ("PMR_access_secret = "+PMRkeys.PMR_access_secret)
h = httplib2.Http(".cache")
# assign variables for headers and content
resp, content = h.request("http://twitter.com/", "GET")
# print response headers
print ("--------------------")
print ("--------response headers------------")
print ()
print (resp)
print ()
print ("--------end response headers--------")
print ("--------------------")
print ()
# extract content type from header >>
content_type = {resp['content-type']}
# assign standard response for utf-8 to test against >>
test_type = {'text/html;charset=utf-8'}
# 
if content_type == test_type :
    print ("Content type = utf-8")
    str_content = content.decode('utf-8')
    print ("contents decoded from utf-8 as...")
    print ("--------------------")
    print ("--------content------------")
    print ()
    print (str_content)
    print ()
    print ("--------end content--------")
    print ("--------------------")
    print ()
else:
    print ("failed with message:")
    print (content_type)

