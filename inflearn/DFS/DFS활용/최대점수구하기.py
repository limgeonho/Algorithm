#최대점수구하기
def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+s[L], time+t[L])
        DFS(L+1, sum, time)

s = list()
t = list()
n, m = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    s.append(a)
    t.append(b)
res = -2147000000
DFS(0, 0, 0)    
print(res)