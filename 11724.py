import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
graph = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    y,x = map(int,input().split())
    graph[y].append(x)
    graph[x].append(y)
    
queue = deque([1])
visited[1] = True
while queue:
    q = queue.popleft()
    print(q)
    for i in sorted(graph[q]):
        if not visited[i]:
            queue.append(i)
            visited[i] = True

       
print(graph)