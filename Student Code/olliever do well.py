from numbers import Number
fileHandle = None
ciphertext = None
plaintext = None
char = None
number = None
fileHandle = open( '\\home\\WorkDropBox\\Code Breaker\\Evidence Folder\\Julius Caeser\\ciphertext.txt', 'r' )
ciphertext = fileHandle.read()
fileHandle.close()
plaintext = ''
for char in ciphertext:
  number = ord( char )
  number = (number if isinstance(number, Number) else 0) + 13
  plaintext = str(plaintext) + str(chr( number ))
print(plaintext)

