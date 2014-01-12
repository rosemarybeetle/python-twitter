import requests
adminURL='https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdGp1NmxJVXVHcGhIel9CNUxJUk8yYXc&output=csv'
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
    
retrieveArray(adminURL)
