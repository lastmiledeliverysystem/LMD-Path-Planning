import pickle
from aStar import aStar
from graphCalculations import addNewNode 

graphFile = open('graphData', 'rb')
graph = pickle.load(graphFile)
graphFile.close()

edgeEqFile = open('graphEqs', 'rb')
edgeEq= pickle.load(edgeEqFile)
edgeEqFile.close()

startPosition = list(map(float, input("Enter start position:").split())) 
goalPosition = list(map(float, input("Enter Goal position:").split())) 

startEdge= addNewNode(startPosition[0],startPosition[1],edgeEq)
start= startEdge.split("->")
start=start[1]

goalEdge= addNewNode(goalPosition[0],goalPosition[1],edgeEq)
goal= goalEdge.split("->")
goal=goal[0]

path = aStar(start, goal, graph)
