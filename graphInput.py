import pickle 
nodes={} #{ "N2":Node}
# nodeCounter = 1
graphFile = open('graphData', 'rb') 
nodes = pickle.load(graphFile) 
nodeCounter = len(nodes.keys()) + 1
print(nodeCounter)
for keys in nodes: 
    print(keys, '=>', nodes[keys]) 
graphFile.close() 

directions={}
while True:
    print("Enter Node Name: ")
    nodeName= input()
    if nodeName =='q':
        break
    print("Enter the postion (x, y): ")
    x, y = map(int, input().split())
    nodePostion=(x, y)
    # print(nodePostion)
    nodeChildren = list(map(str, input("Enter Node's Children:").split())) 
    # print("List of students: ", nodeChildren)
    nodeDirections= list(map(str, input("Enter the Direction for each child(right, left, follow):").split()))
    for i in range (0,len(nodeChildren)):
        directions[nodeChildren[i]]=nodeDirections[i]
    # print(directions)
    print("Decision Node?(Y/N):")
    Decision=input()
    if Decision.upper() == 'Y':
        nodeDecision= True
    else:
        nodeDecision= False
    # print(nodeDecision)

    nodeData={
    "name":nodeName,
    "postion":nodePostion,
    "children":nodeChildren,
    'distances':{},
    "directions":directions,
    "decision":nodeDecision
    }
    nodeName= "N" + str(nodeCounter)
    nodes[nodeName]=nodeData

# Its important to use binary mode 
graphFile = open('graphData', 'wb') 
# source, destination 
# print(nodes['N2'])
pickle.dump(nodes, graphFile)                      
graphFile.close() 
