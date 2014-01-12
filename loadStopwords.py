import requests

stopWords = []
Ws= requests.get('https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdFByYk41am9jRnRkeU9LWnhjZFJTOEE&output=csv')
yy= Ws.text
stopwords = yy.splitlines()

print ('yy --------')
print (yy)
print ('zz --------')
print (stopwords)
print ('--------')
swCount=0
for count in stopwords:
    swCount+=1

print ('count -----')
print (swCount)
