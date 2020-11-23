

graph = {
  'Oradea': [ ['Zerind', 71], ['Sibiu', 151] ],
  'Zerind': [ ['Oradea', 71], ['Arad', 75] ],
  'Arad': [ ['Zerind', 75], ['Timisoara', 118], ['Sibiu', 140] ],
  'Timisoara': [ ['Arad', 118], ['Lugoj', 111] ],
  'Lugoj': [ ['Timisoara', 111], ['Mehadia', 70] ],
  'Mehadia': [ ['Lugoj', 70], ['Drobeta', 75] ],
  'Drobeta': [ ['Mehadia', 75], ['Craiova', 120] ],
  'Sibiu': [ ['Oradea', 151], ['Arad', 140], ['Fagaras', 99], ['Rimnicu Vilcea', 80] ],
  'Rimnicu Vilcea': [ ['Sibiu', 80], ['Craiova', 146], ['Pitesti', 97] ],
  'Craiova': [ ['Drobeta', 120], ['Rimnicu Vilcea', 146], ['Pitesti', 138] ],
  'Fagaras': [ ['Sibiu', 99], ['Bucharest', 211] ],
  'Pitesti': [ ['Rimnicu Vilcea', 97], ['Craiova', 138], ['Bucharest', 101] ],
  'Bucharest': [ ['Fagaras', 211], ['Pitesti', 101], ['Giurgiu', 90], ['Urziceni', 85] ],
  'Giurgiu': [ ['Bucharest', 90] ],
  'Neamt': [ ['Isai', 87] ],
  'Isai': [ ['Neamt', 87], ['Vaslui', 92] ],
  'Vaslui': [ ['Isai', 92], ['Urziceni', 142] ],
  'Urziceni': [ ['Vaslui', 142], ['Bucharest', 85], ['Hirsova', 98] ],
  'Hirsova': [ ['Urziceni', 98], ['Eforie', 86] ],
  'Eforie': [ ['Hirsova', 86] ]
}

distance = { 'Arad':366, 'Bucharest':0, 'Craiova':160, 'Drobeta':242, 'Eforie':161, 'Fagaras':176,
            'Giurgiu':77, 'Hirsova': 151, 'Isai': 226, 'Lugoj':244, 'Mehadia':241, 'Neamt': 234, 'Oradea': 380,
            'Pitesti':100, 'Rimnicu Vilcea': 193, 'Sibiu':253, 'Timisoara': 329, 'Urziceni':80,
            'Vaslui':199, 'Zerind': 374}

explorer = []
frontier = []

frontier.append(['Zerind', 0])

def asterisk():
    while (len(frontier) > 0):
        curNode = frontier[0]
        for i in frontier:
            if distance[i[0]]+i[1] < distance[curNode[0]]+curNode[1]:
                curNode = i
        print("Frontier:", end=" ")
        print("{", end=" ")
        for i in frontier:
            print('(' + str(i[0]) + ',' + str(i[1]), end="), ")
        print("}")
        print("Explorer:", end=" ")
        print("{", end=" ")
        for i in explorer:
            print(i, end=", ")
        print("}")
        print("Expand: " + curNode[0])
        if curNode[0] == 'Bucharest':
            return
        frontier.remove(curNode)
        explorer.append(curNode[0])
        delt = []
        for i in frontier:
            if i[0] == curNode[0]:
                delt.append(i)
        for i in delt:
            frontier.remove(i)
        for i in graph[curNode[0]]:
            if i[0] not in explorer:
                frontier.append([ i[0], i[1]+curNode[1] ])
        print()

def greedyBestFirst():
    while (len(frontier) > 0):
        curNode = frontier[0]
        for i in frontier:
            if distance[i[0]] < distance[curNode[0]]:
                curNode = i
        print("Frontier:", end=" ")
        print("{", end=" ")
        for i in frontier:
            print('(' + str(i[0]) + ',' + str(i[1]), end="), ")
        print("}")
        print("Explorer:", end=" ")
        print("{", end=" ")
        for i in explorer:
            print(i, end=", ")
        print("}")
        print("Expand: " + curNode[0])
        if curNode[0] == 'Bucharest':
            return
        frontier.remove(curNode)
        explorer.append(curNode[0])
        delt = []
        for i in frontier:
            if i[0] == curNode[0]:
                delt.append(i)
        for i in delt:
            frontier.remove(i)
        for i in graph[curNode[0]]:
            if i[0] not in explorer:
                frontier.append([ i[0], i[1]+curNode[1] ])
        print()

def uniFormCostSearch():
    while (len(frontier) > 0):
        curNode = frontier[0]
        for i in frontier:
            if i[1] < curNode[1]:
                curNode = i
        print("Frontier:", end=" ")
        print("{", end=" ")
        for i in frontier:
            print('(' + str(i[0]) + ',' + str(i[1]), end="), ")
        print("}")
        print("Explorer:", end=" ")
        print("{", end=" ")
        for i in explorer:
            print(i, end=", ")
        print("}")
        print("Expand: " + curNode[0])
        if curNode[0] == 'Bucharest':
            return
        frontier.remove(curNode)
        explorer.append(curNode[0])
        delt = []
        for i in frontier:
            if i[0] == curNode[0]:
                delt.append(i)
        for i in delt:
            frontier.remove(i)
        for i in graph[curNode[0]]:
            if i[0] not in explorer:
                frontier.append([ i[0], i[1]+curNode[1] ])
        print()

def bfs():
    while (len(frontier) > 0):
        curNode = frontier[0]
        print("Frontier:", end=" ")
        print("{", end=" ")
        for i in frontier:
            print('(' + str(i[0]) + ',' + str(i[1]), end="), ")
        print("}")
        print("Explorer:", end=" ")
        print("{", end=" ")
        for i in explorer:
            print(i, end=", ")
        print("}")
        print("Expand: " + curNode[0])
        if curNode[0] == 'Bucharest':
            return
        frontier.remove(curNode)
        explorer.append(curNode[0])
        delt = []
        for i in frontier:
            if i[0] == curNode[0]:
                delt.append(i)
        for i in delt:
            frontier.remove(i)
        for i in graph[curNode[0]]:
            if i[0] not in explorer:
                frontier.append([ i[0], i[1]+curNode[1] ])
        print()
        
        
asterisk()