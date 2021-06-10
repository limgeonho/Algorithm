#양팔저울
def DFS(L, sum):
    global res
    if L == n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum + G[L])
        DFS(L+1, sum - G[L])
        DFS(L+1, sum)        

n = input()
G = list(map(int, input().split()))
s = sum(G)
res = set()
DFS(0, 0)
print(s-len(res))