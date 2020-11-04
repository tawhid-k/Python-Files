import string

graph = {
  'A': [['B', 3], ['J', 4], ['G', 1]],
  'B': [['A', 3], ['D', 10]],
  'C': [['H', 3]],
  'D': [['B', 10], ['J', 3], ['H', 11]],
  'E': [['G', 14], ['F', 2], ['I', 1]],
  'F': [['G', 8], ['E', 2], ['I', 2], ['H', 4]],
  'G': [['A', 1], ['J', 6], ['F', 8], ['E', 14]],
  'H': [['D', 11], ['F', 4], ['C', 3], ['I', 6]],
  'I': [['H', 6], ['F', 2], ['E', 1]],
  'J': [['A', 4], ['G', 6], ['D', 3]]
}

explore = []
priority = []
parent = {'A' : 'A'}
cost = {'A' : 1000}

for i in string.ascii_uppercase:
    cost[i] = 1000000
    parent[i] = i

start = 'A' 
goal = 'C'

def uniformSearch():
    if (len(priority) == 0):
        return
    min_node = ['X', 100000000];
    for i in priority:
        if i[1] < min_node[1] and i[0] not in explore:
            min_node = i
    if min_node in priority:
        priority.remove(min_node)
    else:
        return
    explore.append(min_node[0])
    for i in graph[min_node[0]]:
        if i[0] not in explore and cost[i[0]] > cost[min_node[0]] + i[1]:
            cost[i[0]] = cost[min_node[0]] + i[1]
            parent[i[0]] = min_node[0]
            priority.append([i[0], cost[i[0]]])
    uniformSearch()

def showPath(state):
    if (state == start):
        print(state, end="->")
        return
    else:
        showPath(parent[state])
        if (state == goal):
            print(state)
        else:
            print(state, end="->")
    return


cost['A'] = 0
priority.append(['A', 0])
uniformSearch()

print("Minimum cost is: " + str(cost[goal]))
print("The path is given below:")
showPath(goal)


            
    