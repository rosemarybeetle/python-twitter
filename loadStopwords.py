import requests
import json
import csv

stopWords = []
Ws= requests.get('https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdFByYk41am9jRnRkeU9LWnhjZFJTOEE&output=csv')
yy= Ws.text
print (yy)
print ('--------')

jj = csv.reader(yy)
x=0
for el in jj:
    if el != []:
        x+=1
        print (el)
'''for line in yy:
    if line !="\n":
        x=""
        x=x+line
    else:
        print(x)
        x=""
'''
