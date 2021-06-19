#휴가

#최대점수 구하기와 같은 방식으로 휴가일을 선택하는지에 대한 (O, X)문제
def DFS(L, P):
    global res
    if L == n:
        if P > res:
            res = P
    else:
        if L + time[L] <= n:
            DFS(L+time[L], P+pay[L])
        DFS(L+1, P)

n = int(input())

res = -2147000000

time = list()
pay = list()

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

DFS(0, 0)
print(res)