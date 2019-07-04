import pickle
from aStar import aStar
from graphCalculations import addNewNode,generateStartPositions

graphFile = open('graphData', 'rb')
graph = pickle.load(graphFile)
graphFile.close()

edgeEqFile = open('graphEqs', 'rb')
edgeEq= pickle.load(edgeEqFile)
edgeEqFile.close()

startPosition = list(map(float, input("Enter start position:").split())) 
goalPosition = list(map(float, input("Enter Goal position:").split())) 

startEdge= addNewNode(startPosition[0],startPosition[1],edgeEq)
startList= generateStartPositions(startEdge, graph)


goalEdge= addNewNode(goalPosition[0],goalPosition[1],edgeEq)
goal= goalEdge.split("->")
goal=goal[0]

path = aStar(start, goal, graph)
