# filesaver.py
x=0
co = 15
co2=100
f = open('butto.txt', 'r+')
while x<co:
    f.write ('bollox'+str(x)+'\n')
    print ('x = '+str(x))
    x+=1

print ('-----------')
yy=0

while yy < co:
    g=f.readline()
    print('yy = '+str(yy))
    print ('g = '+g)
    yy+=1
print ('yy function complete')  
f.close()

