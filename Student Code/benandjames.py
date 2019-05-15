import neuralNet as neural

myNeuralNetwork = None
netShape = []

netShape.append(2)
netShape.append(5)
netShape.append(5)
netShape.append(2)

myNeuralNetwork = neural.neuralNet(netShape)
myNeuralNetwork.visualise()

fileHandle = None
fileData = None
trainingList = None
fileHandle = open( 'trainingData.txt', 'r' )
fileData = fileHandle.read()
fileHandle.close()
trainingList = fileData.split(',')

fileHandle1 = None
fileData1 = None
trainingLists = None
fileHandle1 = open('trainingTarget.txt', 'r' )
fileData1 = fileHandle1.read()
fileHandle1.close()
trainingLists = fileData1.split(',')

tl = []
for item in trainingLists:
    tl.append(item.split('*'))
    
print(tl)

for lst in item:
    
    
