
import pickle
import math


def aStar(start, goal, graph):
    openList = []
    closedList = []
    path = []

    start = graph[start]
    start['cost'] = 0
    start['totalCost'] = 0

    goal = graph[goal]
    goal['cost'] = 0
    goal['totalCost'] = 0

    openList.append(start)

    def calcHeuristic(node, goal):
        (x1, y1) = node
        (x2, y2) = goal
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    while len(openList):
        currentNode = openList[0]
        currentIndex = 0

while len(openList):

    currentNode = openList[0]
    currentIndex = 0
    print("----------------------------------")
    print("Current Node:", currentNode['name'])

        for index, node in enumerate(openList):
            print("Openning Node", node['name'], "from OpenList")
            # print("node total cost", graph[node]['totalCost'], "current total cost", graph[currentNode]['totalCost'])
            if node['totalCost'] < currentNode['totalCost']:
                currentNode = node
                currentIndex = index
        # print("Before: open", openList,"closed",closedList)
        if currentNode['name'] == goal['name']:
            closedList.append(currentNode)
            print("----------------------------------")
            print("Voilaaaaaaa!")
            break
            # closedList.append(graph[currentNode]['name'])
        openList.pop(currentIndex)
        closedList.append(currentNode)
        # print("After: open", openList,"closed",closedList)

        children = currentNode['children']
        print("Children of", currentNode['name'], ":", children)
        for child in children:
            print("Testing Child", child)
            if child in closedList:
                print("child", child, "is in  closed list, Move on..")
                continue
            #g, h, f
            print("Cost and Heuristic of ", child, ": ")
            h = calcHeuristic(graph[child]['postion'], goal['postion'])
            print("h= ", h)
            g = currentNode['cost'] + currentNode['distances'][child]
            print("g= ", g)
            graph[child]['cost'] = g
            f = g + h
            graph[child]['totalCost'] = f
            print("f= ", f)

            for openNode in openList:
                if child == openNode['name'] and openNode['cost'] < graph[child]['cost']:
                    print("child", child, "is already in the list with less cost")
                    openList.pop((openList.index(graph[child])))
                    continue
            for closeNode in closedList:
                if child == closeNode and graph[closeNode]['cost'] < graph[child]['cost']:
                    print("child", child, "is already in the list with less cost")
                    closedList.pop((closedList.index(graph[child])))
                    continue

            openList.append(graph[child])
            # print("After 2: open", openList,"closed",closedList)
    for node in closedList:
        path.append(node['name'])
    print(path)
    return path
