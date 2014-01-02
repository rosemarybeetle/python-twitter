# get the http client library >>
import httplib2
h = httplib2.Http(".cache")
# assign variables for headers and content
resp, content = h.request("http://twitter.com/", "GET")
# print response headers
print (resp)
print ("--------------------")
# extract content type from header >>
content_type = {resp['content-type']}
# assign standard response for utf-8 to test against >>
test_type = {'text/html;charset=utf-8'}
# 
if content_type == test_type :
    print ("Content type = utf-8")
    str_content = content.decode('utf-8')
    print ("contents decoded from utf-8 as...")
    print (str_content)
else:
    print ("failed with message:")
    print (content_type)
