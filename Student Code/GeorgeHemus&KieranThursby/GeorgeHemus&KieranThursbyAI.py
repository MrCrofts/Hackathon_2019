import neuralNet as neural
netShape = None
fileHandle = None
fileData = None
trainingList = None
reading = None
myNeuralNetwork = None
inputRecord = None
trainingRecords = None
outputRecord = None
targetRecords = None
fileHandle = open( 'trainingData.txt', 'r' )
fileData = fileHandle.read()
fileHandle.close()
trainingList = fileData.split(',')
for reading in []:
  print(reading)
netShape = []
netShape.append(2)
netShape.append(5)
netShape.append(5)
netShape.append(2)
myNeuralNetwork = neural.neuralNet( netShape )
myNeuralNetwork.visualise();inputRecord = []
trainingRecords = []
inputRecord.append(float(-0.794))
inputRecord.append(float(3.173))
trainingRecords.append(inputRecord)
inputRecord[0] = float(-23.549)
inputRecord[1] = float(47.213)
trainingRecords.append(inputRecord)
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

