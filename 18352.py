# import sys
# input = sys.stdin.readline

# N,M,K,X = map(int,input().split())

# # N : 도시의 개수  M : 간선의 개수 K : 거리  X : 출발 도시의 번호 X   
# # X 로부터 출발하여 도달할 수 있는 도시 중 최 단거리가 K 
# # 즉 X부터 K만큼의 최단거리를 가진 노드를 탐색하는 문제임
# #  1 2 => 출발 , 도착으로 보면됨 
# graph = [0 for i in range(M)]
# dis = [i for i in range(M+1)]

# for i in range(M):
#     graph[i] = list(map(int,input().split()))

# result = []
# for i in range(len(graph)):  # 0,1,2,3
#     dis[i] = min(dis[i], dis[i-1] + 1)

#     # x,y = > ex ) 1,3  dis[1] = 1 +1 = 2 < dis[3] = 3
#     # 0 1 2 3 4
#     # 1,3 
#     # 0 1+ 1 = 2 < 3 
#     for x,y in graph:
#         if i == x and  y <= M and dis[i] + 1 < dis[y]:
#             dis[y] = dis[i] + 1
            
# result = []


# for i in range(len(graph)+1):
#     if dis[i] - X == K:
#         result.append(i)
        
# if not result:
#     print(-1)
# else:
#     result.sort()
#     for i in result:
#         print(i)



# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M, K, X = map(int, input().split())

# # 그래프를 인접 리스트로 초기화
# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
#     A, B = map(int, input().split())
#     graph[A].append(B)

# # 거리 정보를 저장할 리스트 초기화
# distance = [-1] * (N + 1)
# distance[X] = 0  # 출발 도시 X의 거리는 0

# # 너비 우선 탐색(BFS) 수행
# queue = deque([X])

# while queue:
#     current_city = queue.popleft()
    
#     for next_city in graph[current_city]:
#         if distance[next_city] == -1:
#             distance[next_city] = distance[current_city] + 1
#             queue.append(next_city)

# # 최단 거리가 K인 도시를 찾아 출력
# result = [i for i in range(1, N + 1) if distance[i] == K]

# if not result:
#     print(-1)
# else:
#     result.sort()
#     for i in result:
#         print(i)




#######################
import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

# 그래프를 인접 리스트로 초기화
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# 거리 정보를 저장할 리스트 초기화
distance = [-1] * (N + 1)
distance[X] = 0  # 출발 도시 X의 거리는 0

queue = deque([X])


while queue:
    
    current_city = queue.popleft()
    for next_city in graph[current_city]:
        if distance[next_city] == -1:
            distance[next_city] = distance[current_city] + 1
            queue.append(next_city)


result = [i for i in range(1, N + 1) if distance[i] == K]

if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)






























        
    