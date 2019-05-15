# Author: M Crofts
# Date: 19/03/19
# Version: 1
'''
neuralNet.py - An abstraction of a simple neural network class which allows a user to instantiate an n by n size network of neurons and weighted connections.
               Each neuron is a simple Sigmoid neuron which may not lend well to some situations.
               Implemented in a class structure for ease of reading by students and maintenance, this approach is not all that efficient. Use of matrices would
               improve efficiency, but obfiscate the functionality to students.
'''

import random, math
from graphics import *

def sigmoid(x):     # Used to sigmoid the result of each neuron
  return 1 / (1 + math.exp(-x))

def antiSigmoid(x):
    return x * ( 1 - x)

class neuralNet():  # The main parent class to hold the neurons and weighted connections
    
    class neuron():
        def __init__(self):             # Constructor for the neuron class
            self.inputLinks = []
            self.bias = random.random() # Initialise bias to a random number between 0 and 1
            self.activatedValue = 0
            self.backPropValue = 0      # Used during backward propogation
            self.x = 0                  # Used for drawing the network
            self.y = 0
            
        def getBias(self):
            return self.bias
        
        def getInputLinks(self):
            return self.inputLinks
        
        def getActivatedValue(self):
            return self.activatedValue
        
        def getX(self):
            return self.x
        
        def getY(self):
            return self.y
        
        def appendInputLink(self, neur):
            self.inputLinks.append(neur)
            
        def activate(self):
            # Calculate the aggregated input weights
            aggregatedInputs = 0
            for neuralL in self.inputLinks:
                aggregatedInputs += (neuralL.getWeight() * neuralL.getSourceNeuron().getActivatedValue())
            aggregatedInputs += self.bias
            # Sigmoid the aggregatedInputs + bias
            self.activatedValue = sigmoid(aggregatedInputs)
            
        def setBias(self, newBias):
            self.bias = newBias
            
        def setX(self, newX):
            self.x = newX
            
        def setY(self, newY):
            self.y = newY
    # End of class neuron()

    class neuralLink():                   # A neural link is the weighted connection between neurons
        
        def __init__(self, neuron):       # Constructor for the neuralLink class
            self.weight = random.random() # Initialise weight to a random number between 0 and 1
            self.sourceNeuron = neuron    # The neuron this link is from, of type neuron()
            self.propogatedWeight = 0.0   # Used in the backward propogation algorithm to temporarily store the new weight value
            self.output = []              # Used to store the output of each neuron in the output layer
            self.maxIn = 0
            
        def getWeight(self):
            return self.weight
        
        def getSourceNeuron(self):
            return self.sourceNeuron
        
        def setWeight(self, newWeight):
            self.weight = newWeight
            
        def updateWeight(self):
            self.weight = self.propogatedWeight
    # End of class neuralLink()
    
    def __init__(self, layerArray):     # Constructor for the neuralNet class
        self.__network = []
        self.learningRate = 0.9
        self.layers = layerArray
        # Create the network based upon number of inputs and layers
        for numberNeurons in layerArray:
            counter = 0
            layerNeurons = []
            for counter in range(0, numberNeurons):
                layerNeurons.append(neuralNet.neuron())
            self.__network.append(layerNeurons)
        # Reset biases for first layer (input layer) to zero, not necessary but nice for the visual representation
        for neuron in self.__network[0]:
            neuron.setBias(0)
        # Create the neural links
        for counter in range(1, len(self.__network)):  # Ignore first layer as it's the input layer
            for neuron in self.__network[counter]:
                for prevNeuron in self.__network[counter -1]:
                    myNeuralLink = neuralNet.neuralLink(prevNeuron)   # Link to the neuron from the previous layer
                    neuron.appendInputLink(myNeuralLink)

    def forwardPropogate(self, inputValues):    # Forward Propogation algorithm for the network
        # Set input values on the input neurons
        for neuronCounter in range(0, len(self.__network[0])):
            self.__network[0][neuronCounter].activatedValue = inputValues[neuronCounter]
        # Activate each neuron from Layer 1 onwards
        for layerCounter in range(1, len(self.__network)):
            currentLayer = self.__network[layerCounter]
            for neuron in currentLayer:
                neuron.activate()
                
    def __calculateError(self, target = [], output = []):   # Calculate the error of the network
        error = []
        for position in range(0, len(target)):
            e = ((target[position] - output[position]) ** 2) * 0.5
            error.append(e)
        return error

    def backwardPropogate(self, inputValues = [], target = []):
        self.output = []
        for neuron in self.__network[len(self.__network) -1]: # Find the output of each of the output neurons
            self.output.append(neuron.getActivatedValue())
        error = self.__calculateError(target, self.output)

        ##########################################
        # Back Propogation

        # Calculate the new weights of the neural links going to the each output neuron
        # The original weights are preserved until the new weights of the entire network
        # have been calculated.
        for outCounter in range(0, len(self.__network[len(self.__network) - 1])):
            outNeuron = self.__network[len(self.__network) - 1][outCounter]
            error = outNeuron.getActivatedValue() - target[outCounter]  # yOut - targetOut
            neuronValue = antiSigmoid(outNeuron.getActivatedValue())    # yOut * (1 - yOut)
            outNeuron.backPropValue = error * neuronValue               # E * ( yOut * (1 - yOut) )
            for neuralLnk in outNeuron.getInputLinks():
                # Calculate the new weight for the link and temporarily store in .propogatedWeight
                connectingNeuronValue = neuralLnk.getSourceNeuron().getActivatedValue()
                weightCorrection = error * neuronValue * connectingNeuronValue
                neuralLnk.propogatedWeight = neuralLnk.getWeight() - ( self.learningRate * weightCorrection )

        # Calculate the new weights of the neural links in the hidden layers
        hiddenLayerCounter = len(self.__network) - 2  # Ignore the output neurons, that calculation happens above
        while hiddenLayerCounter > 0:          # The input layer has no neural link weights to worry about
            for neuroCounter in range(0, len(self.__network[hiddenLayerCounter])):
                neuron = self.__network[hiddenLayerCounter][neuroCounter]
                precedingError = 0.0
                for outCounter in range(0, len(self.__network[hiddenLayerCounter + 1])): # Examine each neuron in the next layer (right) to find the weighted neural link back to this neuron
                    outNeuron = self.__network[hiddenLayerCounter + 1][outCounter]
                    for neuralLnk in outNeuron.getInputLinks():
                        if id(neuralLnk.getSourceNeuron()) == id(neuron):
                            precedingError += outNeuron.backPropValue * neuralLnk.getWeight()
                neuron.backPropValue = precedingError
                for neuralLnk in neuron.getInputLinks():
                    # Calculate the new weight for the link and temporarily store in .propogatedWeight
                    connectingNeuronValue = neuralLnk.getSourceNeuron().getActivatedValue()
                    weightCorrection = neuron.backPropValue * antiSigmoid(neuron.getActivatedValue()) * connectingNeuronValue
                    neuralLnk.propogatedWeight = neuralLnk.getWeight() - ( self.learningRate * weightCorrection )
            hiddenLayerCounter -= 1

        # Set the new weights
        for layer in self.__network:
            for neuron in layer:
                for neuralLnk in neuron.getInputLinks():
                    neuralLnk.updateWeight()         

        ###################################################
    def train(self, inputRecords, targetRecords): # Train the network given the inputs and expected outcomes
      # Normalise the dataset
      maxIn = 0
      for recordArr in inputRecords:
          for data in recordArr:
              if abs(data) > maxIn:
                  maxIn = abs(data)
      self.maxIn = maxIn
      for record in range(0, len(inputRecords)):
          for dataVal in range(0, len(inputRecords[record])):
              inputRecords[record][dataVal] = inputRecords[record][dataVal] / maxIn
      doneLearning = False
      i = 0   # Keeps track of the number of iterations
      currentError = 999998
      prevError = 999999
      numOutputNeurons = len(self.__network[ len(self.__network) - 1 ])
      try:
        while currentError < prevError:  # Stop as soon as the network starts to regress
            sumError = [0] * numOutputNeurons
            correct = 0
            for record in range(0, len(inputRecords)):
                inputValues = inputRecords[record]
                target = targetRecords[record]
                self.forwardPropogate(inputValues)
                self.backwardPropogate(inputValues, target)
                e = self.__calculateError(target, self.output)
                lastError = 0
                for err in sumError:
                  lastError += err
                for errCounter in range(0, len(e)):
                  sumError[errCounter] += e[errCounter]
                totalErr = 0
                for err in sumError:
                  totalErr += err
                change = totalErr - lastError
                recordCorrect = 1
                for outCounter in range(0, len(self.output)):
                  if self.output[outCounter] >= 0.5:
                    self.output[outCounter] = 1
                  else:
                    self.output[outCounter] = 0
                  if self.output[outCounter] != target[outCounter]:
                    recordCorrect = 0
                correct += recordCorrect
            self.learningRate -= 0.05
            if self.learningRate <= 0:
                self.learningRate = 0.05
            accuracy = int( ( correct / len(inputRecords) ) * 100 )
            print("Iteration:", i, "Recordset Error:", sumError, "Accuracy:", str(accuracy) + "%", "change:", change)
            prevError = currentError
            currentError = abs(sumError[0] + sumError[1])
            currentError = float("%.3f" % currentError)
            print("Confidence Level:", "%.3f" % (100 - currentError))
            i += 1
      except KeyboardInterrupt:
        pass
      print("***********************************************")

    def test(self, testRecords, testTargets): # Test the network with new data
      # Normalise the test data
      for record in range(0, len(testRecords)):
          for dataVal in range(0, len(testRecords[record])):
              testRecords[record][dataVal] = testRecords[record][dataVal] / self.maxIn
      correct = 0
      for record in range(0, len(testRecords)):
          inputValues = testRecords[record]
          target = testTargets[record]
          self.forwardPropogate(inputValues)
          output = []
          for neuron in self.__network[len(self.__network) -1]: # Find the output of each of the output neurons
              output.append(neuron.getActivatedValue())

          recordCorrect = 1
          for outCounter in range(0, len(self.output)):
            if self.output[outCounter] >= 0.5:
              self.output[outCounter] = 1
            else:
              self.output[outCounter] = 0
            if self.output[outCounter] != target[outCounter]:
              recordCorrect = 0
          correct += recordCorrect
          
      accuracy = int( ( correct / len(testRecords) ) * 100 )
      print("Accuracy:", str(accuracy) + "%")
      
    def visualise(self):  # Draw the network to the screen, requires graphips.py
      SCREEN_WIDTH = 1024
      SCREEN_HEIGHT = 768
      SPACING = 4
      SPACING_HORIZ = 10

      layers = []
      for counter in range(0, len(self.__network)):
        layers.append( len(self.__network[counter]) )
      neuronWidth = SCREEN_WIDTH / ( len(layers) * SPACING_HORIZ )
      maxHeight = 0
      for layer in layers:
          if layer > maxHeight:
              maxHeight = layer
      neuronHeight = SCREEN_HEIGHT / ( maxHeight * SPACING )
      if neuronWidth < neuronHeight:
          NEURON_SIZE = neuronWidth
      else:
          NEURON_SIZE = neuronHeight
      networkWidth = ( len(layers) * ( NEURON_SIZE * SPACING_HORIZ ) ) - NEURON_SIZE * SPACING_HORIZ
      neuronX = ( SCREEN_WIDTH - networkWidth ) / 2

      # Set up the window
      win = GraphWin("Neural Network", SCREEN_WIDTH, SCREEN_HEIGHT)
      win.setBackground("white")

      for layer in range(0, len(self.__network)):
        neurons = len(self.__network[layer])
        layerSize = NEURON_SIZE * ( neurons * SPACING ) # Vertical Size
        neuronY = ( ( SCREEN_HEIGHT - layerSize ) / 2 ) + ( ( NEURON_SIZE * SPACING ) / 2 )
        for counter in range(0, neurons):
            bias = self.__network[layer][counter].getBias()
            value = self.__network[layer][counter].getActivatedValue()
            self.__network[layer][counter].setX(neuronX)
            self.__network[layer][counter].setY(neuronY)
            neuronDraw = Circle(Point(neuronX, neuronY), NEURON_SIZE)
            neuronBias = Text(Point(neuronX, neuronY - ( NEURON_SIZE / 2 )), "%.3f" % bias)
            neuronBias.setSize(8)
            neuronValue = Text(Point(neuronX, neuronY), "\u03C3=%.3f" % value)
            neuronValue.setSize(8)
            neuronValue.setTextColor("blue")
            neuronDraw.draw(win)
            neuronBias.draw(win)
            neuronValue.draw(win)
            if layer == 0:
                neuralLinkLine = Line( Point(neuronX - NEURON_SIZE, neuronY), Point( neuronX - ( NEURON_SIZE * 2 ), neuronY ) )
                neuralLinkLine.draw(win)
                #inputVal = Text( Point( neuronX - ( NEURON_SIZE * 3 ), neuronY ), inputValues[counter] )
                #inputVal.setSize(8)
                #inputVal.draw(win)
            else: # Not the input layer
                inputNeurons = self.__network[layer][counter].getInputLinks()
                strongestWeight = 0
                # Find the strongest weight
                for neuralLink in inputNeurons:
                    if neuralLink.getWeight() > strongestWeight:
                        strongestWeight = neuralLink.getWeight()
                for neuralLink in inputNeurons:
                    sourceX = neuralLink.getSourceNeuron().getX()
                    sourceY = neuralLink.getSourceNeuron().getY()
                    weight = neuralLink.getWeight()
                    textOffset = 0  # Used to offset the weight text to prevent overtyping
                    if sourceY == neuronY:
                        textOffset = NEURON_SIZE
                    neuralLinkLine = Line( Point(neuronX - NEURON_SIZE, neuronY), Point( sourceX + NEURON_SIZE, sourceY) )
                    #neuralLinkLine.setWidth( ( weight * 10 ) / 3 )
                    if weight == strongestWeight:
                        neuralLinkLine.setOutline("blue")
                    neuralLinkLine.draw(win)
                    linkWeight = Text(Point( ( neuronX - ( NEURON_SIZE * SPACING_HORIZ / 2 ) - textOffset ), ( (neuronY + sourceY) / 2 ) - 8 ), "%.3f" % weight)
                    linkWeight.setTextColor("red")
                    linkWeight.setSize(8)
                    linkWeight.draw(win)
            neuronY += NEURON_SIZE * SPACING
        neuronX += NEURON_SIZE * SPACING_HORIZ
      


if __name__ == '__main__':

  print("This neural network library needs to be imported into your project.")

