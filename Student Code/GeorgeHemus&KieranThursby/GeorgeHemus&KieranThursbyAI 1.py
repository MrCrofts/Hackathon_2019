import neuralNet as neural
netShape = None
myNeuralNetwork = None
inputRecord = None
trainingList = None
fileHandle = None
fileData = None
trainingRecords = None
reading = None
readingList = None
outputRecord = None
counter = None
targetList = None
targetRecord = None
netShape = []
netShape.append(2)
netShape.append(5)
netShape.append(5)
netShape.append(2)
myNeuralNetwork = neural.neuralNet( netShape )
myNeuralNetwork.visualise();inputRecord = []
trainingList = []
fileHandle = open( 'trainingData.txt', 'r' )
fileData = fileHandle.read()
fileHandle.close()
trainingList = fileData.split(',')
trainingRecords = []
for reading in trainingList:
  readingList = reading.split('*')
  counter = 1
  while counter < len(readingList):
    readingList[int(counter - 1)] = float(readingList[int(counter - 1)])
    counter = counter + 1
  trainingRecords.append(readingList)
outputRecord = []
targetList = []
fileHandle = open( 'trainingTarget.txt', 'r' )
fileData = fileHandle.read()
fileHandle.close()
targetList = fileData.split(',')
targetRecord = []
for reading in targetList:
  readingList = reading.split('*')
  counter = 1
  while counter < len(readingList):
    readingList[int(counter - 1)] = float(readingList[int(counter - 1)])
    counter = counter + 1
  targetList.append(readingList)
outputRecord.append(1)
outputRecord.append(0)
targetList.append(outputRecord)
outputRecord[0] = 0
outputRecord[1] = 1
targetList.append(outputRecord)
myNeuralNetwork.train( trainingRecords, targetList )
myNeuralNetwork.visualise();

