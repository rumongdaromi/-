import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
x, y = map(int, input().split())
visited = [[False] * 5 for _ in range(5)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def DFS(x, y,depth,apple):
    visited[x][y] = True
    if graph[x][y] == 1:
        apple += 1
        
    if apple >= 2:
        return 1
    
    if depth > 2: # 깊이가 3인데 아직 APPLE가 2가 안된다면 방문하지않은 것으로 두고 다시 전으로 돌아감
        visited[x][y] = False
        return 0
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visited[nx][ny] and  graph[nx][ny] != -1:
                if DFS(nx,ny,depth + 1, apple) == 1:
                    return 1
            
    visited[x][y] = False
    return 0

print(DFS(x,y,0,0))        
    