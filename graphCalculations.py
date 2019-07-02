import pickle 
import math
from numpy import ones,vstack
from numpy.linalg import lstsq

nodes={} 
#Incidence Matrix
incidenceMatrix=[]

graphFile = open('graphData', 'rb') 
nodes = pickle.load(graphFile) 
for keys in nodes: 
    print(keys, '=>', nodes[keys]) 
graphFile.close() 

def edgeEq(parent,child):
        points = [parent,child]
        x_coords, y_coords = zip(*points)
        A = vstack([x_coords,ones(len(x_coords))]).T
        m, c = lstsq(A, y_coords)[0]
        return m,c


def calcDistance(parent,child):
    parentX, parentY=parent
    childX, childY=child
    # print(parentX,parentY)
    # print(childX,childY)
    distance= math.sqrt((parentX - childX)** 2 + (parentY - childY)** 2)
    # print(distance)
    return distance

#psuedocode#
# For child in each parent
for key in nodes:
    parent= nodes[key]
    # print(parent)
    parentPostion= parent['postion']
    children= parent['children']
    # print(children)
# Find position of that child
    for childName in children:
        child= nodes[childName]
        # print(child)
        childPostion=child['postion']
# Calculate the distance to that child
        distance= calcDistance(parentPostion,childPostion)
        m,c =edgeEq(parentPostion,childPostion)
        print(m,c)
# append that distance in the parent
        parent['distances'][childName]=distance
        print(parent['distances'])


# for key in nodes:
#     parent= nodes[key]
#     children= parent['children']
#     for childName in children:
#         edge= parent['name']+'->'+childName
#     incidenceMatrix.append(edge)
# print(incidenceMatrix)

# graphFile = open('graphData', 'wb') 
# # source, destination 
# # print(nodes['N2'])
# pickle.dump(nodes, graphFile)                      
# graphFile.close() 

