#수들의 조합

#기존의 조합문제와 같다 + sum이라는 변수를 추가해서 배수인지 여부 판단만...
def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1 
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum + a[i])



n, k = map(int, input().split())
a = [0] * k 
for i in range(n):
    p = list(map(int, input().split()))
m = int(input())
cnt = 0
DFS(0, 0, 0)
print(cnt)