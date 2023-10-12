#바닥장식
# 같은 행 -가 2개  -- 일 때 1개로  ㅣ
# 같은 열 ㅣ 가 위아래 2개 일 때    ㅣ 일 떄 1개로 

# 1. 같은게 나오면 계속 해서 옆으로 간다
# 2. 다른게 나오면 함수를 호출해서 y+1 열에서 1번에서 멈춘 곳과 같은 곳과 같으면 또 호출하고 있으면 또 호출 없을 때까지 반복 그리고 도착한 곳은 다른 걸로 표기? 하면 되지않을까
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = []

visited = [[False] * M  for i in range(N)]




for i in range(N):
    graph.append(input())
    
count = 0
x,y = 0,0
def DFS(x,y):
    global count 
    if x >= 0 and x < M and y >= 0 and y < N:
        
    
        for i in range(x+1,M):
            if graph[x][y] == '-':
                
                if graph[i][y] == graph[x][y] and not visited[i][y]:
                    #graph[x][y] = '_' # 문자열은 직접 수정이 안된다는데?
                    visited[x][y] == True 
                    continue
                else:
                    #graph[x][y] = '_'    # 같은 이유   
                    visited[x][y] == True
                    count += 1
        
            
            
            elif graph[x][y] == '|' and graph[x][y+1] == '|':
                for i in range(y+1,N):
                    if graph[x][y] == graph[x][i]:
                        #graph[x][y] = '+' # ㅇㅇ
                        visited[x][y] == True
                        continue
                    elif graph[x][y] != graph[x][i]:
                        visited[x][y] == True
                        #graph[x][y] = '+' # 00 
                        count += 1
                        
DFS(0,0)
print(graph)
print(count)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

visited = [[False] * M for _ in range(N)]

for i in range(N):
    graph.append(input().rstrip())  # 개행 문자 제거

count = 0




