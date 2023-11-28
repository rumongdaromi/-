# import sys
# input = sys.stdin.readline
# from collections import deque
# a = int(input())
# list_q = list(map(int,input().split()))
# #queue = deque()
# # for i in list_q:
# #     queue.append(i)
    
# # 원형 큐 느낌?
# index = 0


# for idx,_ in enumerate(list_q):
#     a = idx   
#     if a < 0: a = len(list_q) - a
#     print(iidx)
#     del list_q[(a) % len(list_q)]
# print(list_q)

# # a = int(input())
# # print(queue[(a) % len(list_q)])

# #음수면 전체길이 -  ( - 음수) 
#=================================================

import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
풍선 = deque(enumerate(map(int,input().split())))

    
for i in range(N):
    idx , val = 풍선.popleft()

    print(idx+1)
    if val > 0:
        풍선.rotate(-(val -1)) #idx => pop
    else:
        풍선.rotate(-val)  
#===================================================    










import sys
input = sys.stdin.readline
#from collections import deque
N = int(input())
풍선 = list(enumerate(map(int,input().split())))
idx = 0
print(풍선)

    
    
while 풍선:
    val = 풍선.pop(idx)
    print(val[0] + 1 , len(풍선),val[1] , idx)

    if val[1] < 0 and 풍선:
        idx = (idx + val[1]) % len(풍선) #  2 + (3,-3) 2 - 3 = -1 % 3 = -4 
    elif val[1] > 0 and 풍선:
        idx = (idx + (val[1] - 1)) % len(풍선) # 위에서 pop으로 인해 길이가 1 줄어듦

list = [1,2,3,4,5,6]

print(list[-1])