print(ord('a'))

graph = [[] for i in range(10)]

graph[1].append(4)
graph[4].append(6)
graph[4].append(3)
graph[3].append(9)
graph[6].append(8)
graph[1].append(2)
graph[2].append(5)
graph[8].append(7)
graph[7].append(1)

def dfs(node, visited): 
    visited.append(node)
    print(node, end = " ")
    for i in graph[node]:
        found = False
        for j in visited:
            if j == i:
                found = True
                break
        if found == False:
            dfs(i, visited)

dfs(1, [])
