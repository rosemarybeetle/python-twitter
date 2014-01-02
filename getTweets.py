import httplib2
h = httplib2.Http(".cache")
resp, content = h.request("http://twitter.com/", "GET")
print (resp)
