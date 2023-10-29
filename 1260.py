import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())

graph = [[] for i in range(N+1)]
visited_DFS = [False] * (N+1)
visited_BFS = [False] * (N+1)
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
    
def DFS(v,graph,visited_DFS):
    visited_DFS[v] = True
    print(v, end = ' ')
    for i in sorted(graph[v]):
        if not visited_DFS[i]:
            DFS(i,graph,visited_DFS)
            
            
            
def BFS(v,graph,visited_BFS):
    queue = deque([v])
    visited_BFS[v] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in sorted(graph[v]):
            if not visited_BFS[i]:
                queue.append(i)
                visited_BFS[i] = True
                
  
DFS(V,graph,visited_DFS)
print()
BFS(V,graph,visited_BFS)