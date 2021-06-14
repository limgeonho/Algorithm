#수열 추측하기

#각각의 이항계수를 구하고 순열을 이용하여 원하는 값이랑 같을 때까지 DFS(O, X 아님)
def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        print()
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum + (p[L] * b[L]))
                ch[i] = 0

n, f = map(int, input().split())
p = [0] * n
b = [1] * n
ch = [0] * (n+1)
for i in range(1, n):
    b[i] = b[i-1] * (n-i) // i
DFS(0, 0)