import pickle
from graphCalculations import addNewNode, generateStartPositions, generateGoalPositions

graphFile = open('graphData', 'rb')
nodes = pickle.load(graphFile)
graphFile.close()
eqFile = open('graphEqs', 'rb')
edgeEqs = pickle.load(eqFile)
eqFile.close()


addNewNode( 4.5, 11.56, nodes, edgeEqs)

