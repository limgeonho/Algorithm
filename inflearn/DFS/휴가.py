#휴가
def DFS(L, sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else: 
        if L + ti[L] <= n+1:
            DFS(L+ti[L], sum+pi[L])
        DFS(L+1, sum)    


n = input()
ti = list()
pi = list()
res = -2147000000

for _ in range(n):
    a, b = map(int, input().split())
    ti.append(a)
    pi.append(b)
ti.insert(0, 0)
pi.insert(0, 0)
DFS(1, 0)
print(res)