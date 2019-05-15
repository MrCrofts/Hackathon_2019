import neuralNet as neural
fileHandle = None
fileData = None
trainingLIst = None
reading = None
netShape = None
inputRecords = None
myNeuralNetwork = None
trainingRecords = None
outputRecord = None
targetRecords = None
fileHandle = open( 'testTarget.txt', 'r' )
fileData = fileHandle.read()
fileHandle.close()
trainingLIst = fileData.split(',')
for reading in trainingLIst:
  print(reading)
netShape = []
netShape.append(2)
netShape.append(5)
netShape.append(5)
netShape.append(2)
inputRecords = []
myNeuralNetwork = neural.neuralNet( netShape )
myNeuralNetwork.visualise();inputRecords = []
trainingRecords = []
inputRecords.append(-0.794)
inputRecords.append(3.173)
trainingRecords.append(inputRecords)
inputRecords[0] = -23.549
inputRecords[1] = 47.213
trainingRecords.append(inputRecords)
outputRecord = []
targetRecords = []
outputRecord.append(1)
outputRecord.append(0)
targetRecords.append(outputRecord)
outputRecord[0] = 0
outputRecord[1] = 1
targetRecords.append(outputRecord)
myNeuralNetwork.train( trainingRecords, targetRecords )
myNeuralNetwork.visualise();

