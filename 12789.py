import sys
import copy
input = sys.stdin.readline

from collections import deque
N = int(input())
q = list(map(int,input().split()))
나 = 1

줄서는곳 = deque()
for i in q:
    줄서는곳.append(i)
간식받는곳 = []

한명씩설수있는공간 = deque()

# print(줄서는곳.popleft()) # ==5
while 줄서는곳:
    if 줄서는곳 and 줄서는곳[0] == 나:
        줄서는곳.popleft()
        나 += 1
    else:
        한명씩설수있는공간.append(줄서는곳.popleft())
    
    while 한명씩설수있는공간 and 한명씩설수있는공간[-1] == 나:
        한명씩설수있는공간.pop()
        나 += 1

if 한명씩설수있는공간:
    print('Sad')
else:
    print('Nice')


 


