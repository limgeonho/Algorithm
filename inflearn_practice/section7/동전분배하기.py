#동전분배하기

# 사람 수 만큼 DFS를 돌려서 동전을 선택하는 문제, (O, X)아님
def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha

    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]

n = int(input())
coin = list()
tmp = list()
money = [0] * 3
res = -2147000000
for _ in range(n):
    coin.append(int(input()))

DFS(0)
print(res)