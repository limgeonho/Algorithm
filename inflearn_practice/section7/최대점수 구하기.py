#최대점수 구하기

#다음문제를 푸는 지 풀지 않는지에 대한 선택(O, X)문제
def DFS(L, time, sum):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, time + t[L], sum + v[L])
        DFS(L+1, time, sum)


n, m = map(int, input().split())
v= list()
t = list()
for _ in range(n):
    a, b = map(int, input().split())
    v.append(a)
    t.append(b)
res = -2147000000

DFS(0, 0, 0)
print(res)