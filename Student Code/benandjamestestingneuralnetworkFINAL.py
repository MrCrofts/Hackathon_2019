import neuralNet as neural

myNeuralNetwork = None
netShape = []

netShape.append(2)
netShape.append(5)
netShape.append(5)
netShape.append(2)

myNeuralNetwork = neural.neuralNet(netShape)
myNeuralNetwork.visualise()

fileHandle0 = None
fileData0 = None
trainingList0 = None
fileHandle0 = open( 'testData.txt', 'r' )
fileData0 = fileHandle0.read()
fileHandle0.close()
testList = fileData0.split(',')

testd = []
for item in testList:
    testd.append(item.split('*'))

testData = []
for lst in testd:
    sc=[]
    sc.append(float(lst[0]))
    sc.append(float(lst[1]))
    testData.append(sc)
    

fileHandle5 = None
fileData5 = None
trainingList5 = None
fileHandle5 = open( 'testTarget.txt', 'r' )
fileData5 = fileHandle5.read()
fileHandle5.close()
testDataTarget = fileData5.split(',')

testdt = []
for item in testDataTarget:
    testdt.append(item.split('*'))
    
testTarget=[]
for lst in testdt:
    sc.append(int(lst[0]))
    sc.append(int(lst[1]))
    testTarget.append(sc)
    

fileHandle = None
fileData = None
trainingList = None
fileHandle = open( 'trainingData.txt', 'r' )
fileData = fileHandle.read()
fileHandle.close()
trainingList = fileData.split(',')

td = []
for item in trainingList:
    td.append(item.split('*'))
    
trainingData = []
for lst in td:
    sc=[]
    sc.append(float(lst[0]))
    sc.append(float(lst[1]))
    trainingData.append(sc)

print(trainingData)
    

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
    

trainingTarget=[]
for lst in tl:
    sc = []
    sc.append(int(lst[0]))
    sc.append(int(lst[1]))
    trainingTarget.append(sc)
    
print(trainingTarget)

myNeuralNetwork.train(trainingData,trainingTarget)
myNeuralNetwork.test(testData,testTarget)

