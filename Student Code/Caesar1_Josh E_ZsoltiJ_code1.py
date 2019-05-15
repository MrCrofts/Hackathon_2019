#Caesar Cypher
#By Joshua Everett (with advise from Zsolti J)
#v1

filehandle=None
ciphertext=None
filehandle=open('/home/WorkDropBox/Code Breaker/Evidence Folder/Julius Caesar/ciphertext.txt','r')
ciphertext=filehandle.read()
filehandle.close()

FText=""
NText=ciphertext.split(" ")
for x in range(len(NText)):
    for i in range(len(NText[x])):
        a=(ord(NText[x][i]))
        c=a+13
        if a>77:
            b=a-13
        else:
            b=a+13
        if a < 65:
            b=a
        FText=FText+chr(b)
    FText=FText+" "

print(FText)

            
        
