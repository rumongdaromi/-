import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N+1)]
dist = [0 for _ in range(N+1)]

for i in range(1,N):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
    
# def DFS(u,graph):
#     visited[u] = True
#     for v,w in graph[u]:
#         if not visited[v]:
#             dist[v] = dist[u] + w
#             DFS(v,graph)
#     return

def BFS(graph,visited,u):
    queue = deque([u])
    visited[u] = True
    while queue:
        u = queue.popleft()
        for v,w in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                dist[v] = dist[u] + w
        
    
#print(graph)
BFS(graph,visited,1)
print(max(dist))
#print(dist)
# DFS(1,graph)
# print(max(dist))
# print(graph)
# print(dist)


# N = int(input())
# #graph = [[] for _ in range(N)]
# graph = [list(map(int, input().split())) for _ in range(N-1)] #입력해서 리스트에 삽입
# #distance = [100 for i in range(N+1)]
# dist = [float("inf") for _ in range(N+1)] # 최단 경로 저장 5 150

# for i in range(N+1):
#     #dist[i] = min(dist[i],dist[i-1]+1)
#     for u,v,w in graph:
#         if i == u and v <= N:
#             if dist[u] < inf and  dist[v] >= dist[u] + w:
#                 dist[v] = dist[u] + w
# print(dist)

# 1,2,3,4

# 4
# 1 2 3
# 2 3 2
# 2 4 4
# for i in range(1,N):
#     u,v,w = map(int,input().split())
#     graph[u].append(v)
    
#     for i in dist:
#         if dist[v] >= dist[u] + w:
#             if dist[u] < inf:
#                 dist[v] = w + dist[u] 
#             else:
#                 dist[v] = w


# for i in range(1,N-1):
#     if u == i and v <= N and distance[i] + w <= distance[v]:
#         u,v,w = map(int,input().split())
#         distance[v] = distance[i] + w
#         graph[u] = (v,w)

