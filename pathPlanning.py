import pickle
from aStar import aStar

graphFile = open('graphData', 'rb')
graph = pickle.load(graphFile)
graphFile.close()

start = str(input("Enter the start node:"))
goal = str(input("Enter the Goal node:"))

path = aStar(start, goal, graph)
