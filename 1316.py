import sys
n = int(sys.stdin.readline())
ans = n
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if  word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            ans = ans - 1
            break
            
print(ans)
        