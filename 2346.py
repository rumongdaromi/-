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
    
    # queue.popleft()
    # print(a)
    # if a >= 0: 
    #     queue[a]
    #     queue.rotate(-a * -1)
    # else:
    #     queue[a]
    #     queue.rotate(a)

#음수면 전체길이 -  ( - 음수)   3 2 1 -3 -1  2 1 -3 -1   -3 -1 2 1   1 -1 2