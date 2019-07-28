
import pickle
import math


def calcHeuristic(node, goal):
    (x1, y1) = node
    (x2, y2) = goal
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def reconstructPath(closedList, graph):
    path = []
    goal = closedList[-1]
    start = closedList[0]
    path.append(goal)
    goalParents = graph[goal]['parents']
    while start not in goalParents:
        for parent in goalParents:
            if parent in closedList and parent not in path:
                path.append(parent)
                goalParents = graph[parent]['parents']
    path.append(start)
    return path[::-1]
    # path.append(closedList[-1])
    # closedList = closedList[::-1]
    # print(closedList)
    # for Node in closedList:
    #     parents = graph[Node]['parents']
    #     for parent in parents:
    #         if parent in closedList and parent not in path:
    #             path.append(parent)
    # return path[::-1]


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

    while len(openList):
        currentNode = openList[0]
        currentIndex = 0

        print("----------------------------------")
        print("Current Node:", currentNode['name'])

        for index, node in enumerate(openList):
            # print("Openning Node", node['name'], "from OpenList")
            # print("node total cost", graph[node]['totalCost'], "current total cost", graph[currentNode]['totalCost'])
            if node['totalCost'] < currentNode['totalCost']:
                currentNode = node
                currentIndex = index
        # print("Before: open", openList,"closed",closedList)
        if currentNode['name'] == goal['name']:
            closedList.append(currentNode)
            print("----------------------------------")
            print("Voilaaaaaaa!")
            for node in closedList:
                path.append(node['name'])
            print("Path befor reconstruction", path)
            path = reconstructPath(path, graph)
            return path
            # closedList.append(graph[currentNode]['name'])
        openList.pop(currentIndex)
        closedList.append(currentNode)
        # for Node in openList:
        #     print("Open List", Node['name'])
        # for Node in closedList:
        #     print("Close List", Node['name'])

        # print("After: open", openList,"closed",closedList)
        if currentNode['name'] == ' None':
            continue
        children = currentNode['children']
        # print("Children of", currentNode['name'], ":", children)
        for child in children:
            print("Testing Child", child)
            if child in closedList:
                print("child", child, "is in  closed list, Move on..")
                continue
            #g, h, f
            # print("Cost and Heuristic of ", child, ": ")
            if child == 'None':
                graph[child]['totalCost'] = 100000
                graph[child]['cost'] = 100000
            else:
                h = calcHeuristic(graph[child]['position'], goal['position'])
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
    return '7eta sad'
