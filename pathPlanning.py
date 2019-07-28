import pickle
from aStar import aStar
from graphCalculations import addNewNode, generateStartPositions, generateGoalPositions, checkNode

graphFile = open('graphData', 'rb')
graph = pickle.load(graphFile)
graphFile.close()

edgeEqFile = open('graphEqs', 'rb')
edgeEq = pickle.load(edgeEqFile)
edgeEqFile.close()


# for keys in edgeEq:
#     print(keys, "=>", edgeEq[keys])
def planPath(startPosition,goalPosition):
    startList = []
    goalList = []
    startNode = checkNode(startPosition[0], startPosition[1], graph)
    if startNode == -1:
        startEdge = addNewNode(startPosition[0], startPosition[1], graph, edgeEq)
        print("start edge", startEdge)
        startList = generateStartPositions(startEdge, graph)
    else:
        startList.append(startNode)

    goalNode = checkNode(goalPosition[0], goalPosition[1], graph)
    if goalNode == -1:
        goalEdge = addNewNode(goalPosition[0], goalPosition[1], graph, edgeEq)
        print("goal edge", goalEdge)
        goalList = generateGoalPositions(goalEdge, graph)
    else:
        goalList.append(goalNode)


    paths = []
    for i in range(0, len(startList)):
        for j in range(0, len(goalList)):
            tempPath = aStar(startList[i], goalList[j], graph)
            if tempPath != '7eta sad':
                paths.append(tempPath)


    print("Start", startList)
    print("Goal", goalList)

    for i in range(0, len(paths)):
        print("Path #", i, "is:", paths[i])

    listLengths = []
    for path in paths:
        listLengths.append(len(path))
    shortestPath = paths[listLengths.index(min(listLengths))]
    print("----------------------------")
    print("The shortest path:", shortestPath)
    return shortestPath
    
if __name__ == "__main__":
    startPosition = list(map(float, input("Enter start position:").split()))
    goalPosition = list(map(float, input("Enter Goal position:").split()))
    planPath(startPosition,goalPosition)