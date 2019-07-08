import pickle
import math
from numpy import ones, vstack
from numpy.linalg import lstsq


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
    m = round(m, 2)
    c = round(c, 2)
    print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
    return m, c


def calcDistance(parent, child):
    parentX, parentY = parent
    childX, childY = child
    distance = math.sqrt((parentX - childX) ** 2 + (parentY - childY) ** 2)
    return distance


def checkNode(x, y, nodes):
    threshold = 0.05
    for key in nodes:
        if nodes[key]['name'] == "None":
            continue
        nodePosition = nodes[key]['position']
        nodePosition[0] = round(nodePosition[0], 2)
        nodePosition[1] = round(nodePosition[1], 2)
        distance = calcDistance((x, y), nodePosition)
        if distance <= threshold:
            print(nodes[key]['name'])
            return nodes[key]['name']
    return -1


def addNewNode(x, y, nodes, edgeEqs):
    newPoint = [x, y]
    edges = []
    edgeEq = ''
    goalEdges = []

    for key in edgeEqs:
        eq = edgeEqs[key]
        res = eq[0] * x + eq[1] - y
        res = round(res, 1)
        # print(key, "=>", res)
        if (abs(res) <= .5):
            edges.append((key, res))
    for i in range(0, len(edges)):
        edge1 = edges[i][0].split('->')[0]  # start edge
        edge2 = edges[i][0].split('->')[1]  # end edge
        partDistance1 = round(calcDistance(
            nodes[edge1]['position'], newPoint), 1)
        partDistance2 = round(calcDistance(
            nodes[edge2]['position'], newPoint), 1)
        totalDistance = round(calcDistance(
            nodes[edge1]['position'], nodes[edge2]['position']), 1)
        print("part1", partDistance1, "part2",
              partDistance2, "total", totalDistance)
        if round(partDistance1 + partDistance2, 1) <= totalDistance:
            # startEdges.append(edge1)
            # goalEdges.append(edge2)
            edgeEq = edge1 + "->" + edge2
            print("edge", edge1, edge2)
            print("located")
        # print(edge)
    print("edges in add new node", edges)
    return edgeEq


def generateStartPositions(startEdge, nodes):
    print("startedge ingenerate", startEdge)
    startEdge = startEdge.split("->")
    # for i in range(0, len(startEdge)):
    parentNode = startEdge[0]
    children = nodes[parentNode]['children']
    return children


def generateGoalPositions(goalEdge, nodes):
    print("goaledge ingenerate", goalEdge)
    goalEdge = goalEdge.split("->")
    # for i in range(0,len(goalEdge)):
    childNode = goalEdge[1]
    parents = nodes[childNode]['parents']
    return parents

#psuedocode for distance calculation#
# 1- For child in each parent
# 2- Find position of that child
# 3- Calculate the distance to that child
# 4- append that distance in the parent


if __name__ == "__main__":
    nodes = {}
    edgeEqs = {}

    graphFile = open('graphData', 'rb')
    nodes = pickle.load(graphFile)

    # for key in nodes:
    #     print("-------------- Graph Nodes --------------")
    #     print(position)
    #     print(keys, '=>', nodes[keys])

    for nodeName in nodes:
        parent = nodes[nodeName]
        # print(parent)
        parentPostion = parent['position']
        children = parent['children']
        # print(children)
        for childName in children:
            if childName == "None":
                parent['distances'][childName] = 100000
            else:
                child = nodes[childName]
                # print(child)
                childPostion = child['position']
                # Distance Calulations #
                distance = calcDistance(parentPostion, childPostion)
                parent['distances'][childName] = distance
                # print(parent['distances'])

                # Edge Calculations #
                edgeName = parent['name']+'->'+childName
                # Edge Equation Calculation #
                m, c = calcEdgeEq(parentPostion, childPostion)
                # print("m",m,"c",c)
                edgeEqs[edgeName] = (m, c)

    # for key in edgeEqs:
    #     print(key, '=>', edgeEqs[key])

    graphFile = open('graphData', 'wb')
    graphEquations = open('graphEqs', 'wb')
    pickle.dump(nodes, graphFile)
    pickle.dump(edgeEqs, graphEquations)
    graphFile.close()
    graphEquations.close()
