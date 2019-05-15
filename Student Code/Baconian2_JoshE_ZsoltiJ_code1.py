#By Joshua Everett
#Baconian Cypher
#v1

import textwrap

filehandle=None
ciphertext=None
filehandle=open('/home/WorkDropBox/Code Breaker/Evidence Folder/Trinity/ciphertext.txt','r')
ciphertext=filehandle.read()
filehandle.close()




NText=ciphertext[1:]
layer1=""
for char in NText:
    if ord(char) > 64 and ord(char) < 91:
        layer1+="1"
    else:
        layer1+="0"

NText=ciphertext
layer1=""
for char in NText:
    if ((ord(char) > 64) and (ord(char) < 91)):
        layer1=layer1+"1"
    if ((ord(char) > 96) and (ord(char) < 123)):
        layer1=layer1+"0"


        
newLayer1 = layer1.replace(" ","")

newNewLayer1 = " ".join(textwrap.wrap(newLayer1, 5))
layer1list=newNewLayer1.split()
print(layer1list)



counter = 0
number = 0
countLimit = len(layer1list) / 6
final = ""

while counter < countLimit - 1:
    number=0
    layer3=str(layer1list[counter])
    if layer3[4] == '1':
        number += 1
    if layer3[3] == '1':
        number += 2
    if layer3[2] == '1':
        number += 4
    if layer3[1] == '1':
        number += 8
    if layer3[0] == '1':
        number += 16
    
    final=final+chr(number+65)
    counter+=1

print(final)
