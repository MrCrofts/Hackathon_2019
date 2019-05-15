from numbers import Number
fileHandle = None
ciphertext = None
plaintext = None
ultCount = None
key = None
char = None
number = None
difference = None
fileHandle = open( '/home/WorkDropBox/Code Breaker/Evidence Folder/Giovan Battista Bellaso/ciphertext.txt', 'r' )
ciphertext = fileHandle.read()
fileHandle.close()
plaintext = ''
ultCount = 0
key = 'ULTIMECIA'
for char in ciphertext:
  number = ord( char )
  if number >= 65 and number <= 90:
    number = (number if isinstance(number, Number) else 0) + -65
    difference = number - (ord( (key[int(ultCount - 1)]) ) - 65)
    ultCount = (ultCount if isinstance(ultCount, Number) else 0) + 1
    if ultCount > 8:
      ultCount = 0
    if difference < 0:
      difference = (difference if isinstance(difference, Number) else 0) + 26
    print(chr( (difference + 65) ))
  if number >= 97 and number <= 122:
    number = (number if isinstance(number, Number) else 0) + -97
    difference = number - (ord( (key[int(ultCount - 1)]) ) - 65)
    ultCount = (ultCount if isinstance(ultCount, Number) else 0) + 1
    if ultCount > 8:
      ultCount = 0
    if difference < 0:
      difference = (difference if isinstance(difference, Number) else 0) + 26
    print(chr( (difference + 65) ))

