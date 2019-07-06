import pickle
from aStar import aStar
from graphCalculations import addNewNode, generateStartPositions, generateGoalPositions

graphFile = open('graphData', 'rb')
graph = pickle.load(graphFile)
graphFile.close()

edgeEqFile = open('graphEqs', 'rb')
edgeEq = pickle.load(edgeEqFile)
edgeEqFile.close()

# for keys in edgeEq:
#     print(keys, "=>", edgeEq[keys])

startPosition = list(map(float, input("Enter start position:").split()))
goalPosition = list(map(float, input("Enter Goal position:").split()))

startEdge= addNewNode(startPosition[0], startPosition[1], graph, edgeEq)
print("start edge", startEdge)
startList = generateStartPositions(startEdge, graph)
print(startList)

goalEdge = addNewNode(goalPosition[0], goalPosition[1],graph, edgeEq)
print("goal edge", goalEdge)
goalList = generateGoalPositions(goalEdge, graph)
print(goalList)
path= []
for i in range(0, len(startList)):
    for j in range(0, len(goalList)):
        path.append(aStar(startList[i], goalList[j], graph))

for i in range(0,len( path)):
         print("Path #",i,"is:",path[i])
minList = min((x) for x in path)
print("----------------------------")
print("The shortest path:", minList)