'''
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
The function should return the length of the shortest path between A and B. 
Consider the length as the number of edges in the path, not the number of nodes. 
If there is no path between A and B, then return -1.
'''

# performing level order travel by bfs to store node and distance and finally return distance. 
from collections import defaultdict, deque

def shortest_path(edges, node_A, node_B):
  adjl = defaultdict(dict)
  for u,v in edges:
    adjl[u][v]=1
    adjl[v][u]=1
  
  visited = set([node_A])
  queue = deque([(node_A,0)])
  
  while len(queue) > 0:
    node, dist = queue.popleft()
    
    if node == node_B:
      return dist
    
    for i in adjl[node]:
      if i not in visited:
        visited.add(i)
        queue.append((i,dist+1))
  return -1
