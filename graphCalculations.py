import pickle
import math
from numpy import ones, vstack
from numpy.linalg import lstsq

nodes = {}
edgeEqs = {}
# Incidence Matrix

graphFile = open('graphData', 'rb')
nodes = pickle.load(graphFile)
graphFile.close()


for keys in nodes:
    print("-------------- Graph Nodes --------------")
    print(keys, '=>', nodes[keys])


def edgeEq(parent, child):
    points = [parent, child]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords)[0]
    return m, c


def calcEdgeEq(parent, child):
    points = [parent, child]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords)[0]
    print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
    return m, c


def calcDistance(parent, child):
    parentX, parentY = parent
    childX, childY = child
    # print(parentX,parentY)
    # print(childX,childY)
    distance = math.sqrt((parentX - childX) ** 2 + (parentY - childY) ** 2)
    print(distance)
    return distance


def addNewNode(x, y, edgeEqs):
    for key in edgeEqs:
        eq = edgeEqs[key]
        res = eq[0] * x + eq[1] - y
        print(res)
        if (res == 0):
            return key

#psuedocode for distance calculation#
# 1- For child in each parent
# 2- Find position of that child
# 3- Calculate the distance to that child
# 4- append that distance in the parent


for nodeName in nodes:
    parent = nodes[nodeName]
    # print(parent)
    parentPostion = parent['postion']
    children = parent['children']
    # print(children)
    for childName in children:
        child = nodes[childName]
        print(child)
        childPostion = child['postion']

        # Distance Calulations #
        distance = calcDistance(parentPostion, childPostion)
        parent['distances'][childName] = distance
        print(parent['distances'])

        # Edge Calculations #
        #edgeName= parent['name']+'->'+childName

        # Edge Equation Calculation #
        #m,c = calcEdgeEq(parentPostion, childPostion)
        # print("m",m,"c",c)
        # edgeEqs[edgeName]=(m,c)


# for key in edgeEqs:
#     print(key, '=>', edgeEqs[key])

#print("The new node is on ", addNewNode(2.5, 2.5, edgeEqs))

graphFile = open('graphData', 'wb')
graphEquations = open('graphEqs', 'wb')
pickle.dump(nodes, graphFile)
pickle.dump(edgeEqs, graphEquations)
graphFile.close()
graphEquations.close()
