import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = 5,5

graph = [list(map(int, input().split())) for _ in range(5)]
x, y = map(int, input().split())

visited = [[False] * 5 for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y,depth,apple):
    visited[x][y] = True
    if apple >= 2:
        return 1
    
    if depth > 2: # 깊이가 3인데 아직 APPLE가 2가 안된다면 방문하지않은 것으로 두고 다시 전으로 돌아감
        visited[x][y] = False
        return 0
    
        
    
    if graph[x][y] == 1:
        apple += 1
    
    for i in range(4):
        nx = dx + x
        ny = dy + y
        
        if not (nx < 0 or ny > 5 or nx > 5 or ny < 0):
            if visited[nx][ny] == False and  graph[nx][ny] == -1:
                DFS(nx,ny,depth + 1, apple)
                return 1
            
    visited[x][y] = False
    return 0

print(DFS(x,y,0,0))        
    