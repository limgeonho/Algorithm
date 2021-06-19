#동전 바꿔주기

#각각의 동전의 개수만큼 돌면서 선택하는 문제, (O, X)아님
def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt+=1
    else:
        for i in range(n[L]+1):
            DFS(L+1, sum+(p[L]*i) )

t = int(input())
k = int(input())
p = list()
n = list()
cnt = 0
for _ in range(k):
    a, b = map(int, input())
    p.append(a)
    n.append(b)

DFS(0, 0)
print(cnt)