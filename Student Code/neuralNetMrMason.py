import neuralNet as neural
fileHandle = None
fileData = None
trainingList = None
reading = None
netShape = None
inputRecords = None
myNeuralNetwork = None
inputRecord = None
targetRecords = None
fileHandle = open( 'trainingData.txt', 'r' )
fileData = fileHandle.read()
fileHandle.close()
trainingList = fileData.split(',')
for reading in trainingList:
  print(reading)
netShape = []
netShape.append(2)
netShape.append(5)
netShape.append(5)
netShape.append(2)
inputRecords = []
myNeuralNetwork = neural.neuralNet( netShape )
myNeuralNetwork.visualise();inputRecord = []
targetRecords = []

