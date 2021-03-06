from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import csv

class KNNClassify :
    complexity = 0;
    numInputs = 0;
    discreteOutput = 0;
    discreteInputs = [];
    numObservations = 0;
    x_Obs = np.empty([0, 0]);
    y_Obs = np.empty([0]);
    y_Test = np.empty([0]);

    neigh = KNeighborsClassifier(n_neighbors=11, weights='distance')

    def __init__(self, complexity, numInputs, discreteOutputs, discreteInputs):
        self.complexity = complexity;
	self.numInputs = numInputs;
	self.discreteOutputs = discreteOutputs;
	self.discreteInputs = discreteInputs;
	self.x_Obs = np.empty([0,numInputs]);
	self.x_Test = np.empty([0,numInputs]);
	
    def addSingleObservation(self, newInputObs, newOutputObs):
        if (len(newInputObs) == self.numInputs and type(newOutputObs) not in (tuple, list)):
            print("All good!");
            self.x_Obs = np.vstack((self.x_Obs,newInputObs));
            self.y_Obs = np.append(self.y_Obs, newOutputObs);
            self.numObservations += 1;
	else:
            print("Wrong dimensions!");

    def addBatchObservations(self, newInputObsMatrix, newOutputVector):
        if(len(newInputObsMatrix.shape) == 2 and newInputObsMatrix.shape[1] == self.numInputs and newOutputVector.shape[0] == newInputObsMatrix.shape[0]):
            print("All good!");
            newOutputVector = newOutputVector.ravel();
            i = 0;
            for newInputVector in newInputObsMatrix:
                newOutputValue = newOutputVector[i];
		self.addSingleObservation(newInputVector, newOutputValue);
		i += 1;
	else:
            print("Wrong dimensions!");

    def train(self):
        if (self.numObservations > 0):
            print("Training started");
            self.neigh.fit(self.x_Obs, self.y_Obs);
            return True;
        else:
            print("Not enough observations to train!");
            return False;

    def execute(self, inputObsVector):
        if(len(inputObsVector) == self.numInputs):
            print("Begin execute");
            x_Test = np.reshape(inputObsVector,(1,self.numInputs));
            self.y_Test = self.neigh.predict(x_Test);
            return self.y_Test;
        else:
            print("Wrong dimensions, fail to execute");
            return None;
        
