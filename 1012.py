import sys
sys.setrecursionlimit(10000) 
input = sys.stdin.readline
count = 0
  
def DFS(graph,x,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for i in range(4):
        x_dx = x + dx[i]
        y_dy = y + dy[i]
        if y_dy >= 0 and y_dy < N and x_dx >= 0 and x_dx < M:
            if graph[y_dy][x_dx] == 1:
                graph[y_dy][x_dx] = 0
                DFS(graph,x_dx,y_dy)                     



T = int(input())

for _ in range(T):
    count = 0
    M,N,K = map(int,input().split())
    graph = [[0] * (M) for _ in range(N)]   
    for i in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1


    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                DFS(graph,i,j)
                count += 1        
    print(count)



#========================

# import sys
# input = sys.stdin.readline

# M,N,K = map(int,input().split())

# graph = [[0] * (M+1) for _ in range(N+1)]
# #visited= [[False] * (M+1) for _ in range(N+1)]

# x,y = 0,0
# count = 0
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# for i in range(K):
#     x,y = map(int,input().split())
#     graph[y][x] = 1
    
# def DFS(visited,graph,count,x,y):
#     if y_dy >= 0 and y_dy <= N and x_dx >= 0 and x_dx <= M:
#         if not visited[y][x]:
#             visited[y][x] = True
#             if graph[y][x] == 1:
#                 graph[y][x] = 0
#                 for i in range(4):
#                     x_dx = x + dx[i]
#                     y_dy = y + dy[i]                    
#                     if graph[y_dy][x_dx] == 1:
#                         DFS(visited,graph,count,x_dx,y_dy)
#                         return True
    
#     else:
#         return False


# DFS(visited,graph,count,1,1)

# print(visited)


