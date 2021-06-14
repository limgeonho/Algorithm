#동전교환

#중복순열처럼 여러가지 동전중에서 하나를 고르고 계속해서 L값을 증가시킴(O, X 아님)
def DFS(L, sum):
    global res
    if L >= res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res: 
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum + a[i])


n = int(input())

a = list(map(int, input().split()))

m = int(input())

res = 2147000000
#그리디처럼 액수가 큰 동전부터 탐색
a.sort()
DFS(0, 0)

print(res)
