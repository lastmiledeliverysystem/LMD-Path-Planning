import pickle
nodes = {}  # { "N2":Node}
nodeCounter = 1
graphFile = open('graphData', 'rb')
nodes = pickle.load(graphFile)
nodeCounter = len(nodes.keys()) + 1
print(nodeCounter)
for keys in nodes:
    if nodes[keys]['name'] == 'None':
        continue
    print(keys, "=>", nodes[keys]['parents'])
graphFile.close()

directions = {}

while True:
    print("Enter Node Name: ")
    nodeName = input()
    if nodeName == 'q':
        break
    print("Enter the postion (x, y): ")
    x, y = map(float, input().split())
    nodePosition = [x, y]    # print(nodePosition)
    directions = {}
    nodeParent = []
    nodeParent = list(map(str, input("Enter Node's Parents:").split()))
    nodeChildren = []
    nodeChildren = list(map(str, input("Enter Node's Children:").split()))
    nodeDirections = list(map(str, input(
        "Enter the Direction for each child(right, left, follow):").split()))
    # print(nodeDirections)
    for i in range(0, len(nodeChildren)):
        if nodeDirections[i].upper() == "R":
            nodeDirections[i] = "right"
        if nodeDirections[i].upper() == "L":
            nodeDirections[i] = "left"
        if nodeDirections[i].upper() == "F":
            nodeDirections[i] = "follow"
        directions[nodeChildren[i]] = nodeDirections[i]
    # print(directions)
    nodeDecision = {}
    decisionList = []
    decisionList = list(map(str, input("Enter Node's Decision:").split()))
    #print("node children",nodeChildren)
    for i in range(0, len(decisionList)):
        if decisionList[i].upper() == 'Y':
            decisionList[i] = True
        else:
            decisionList[i] = False
        nodeDecision[nodeChildren[i]] = decisionList[i]
        # print(nodeDecision)

    nodeData = {
        "name": nodeName,
        "position": nodePosition,
        "parents": nodeParent,
        "children": nodeChildren,
        'distances': {},
        "directions": directions,
        "decision": nodeDecision,
    }
    # nodeName= "N" + str(nodeCounter)
    nodes[nodeName] = nodeData

# Its important to use binary mode
graphFile = open('graphData', 'wb')
# source, destination
# print(nodes['N2'])
pickle.dump(nodes, graphFile)
graphFile.close()
