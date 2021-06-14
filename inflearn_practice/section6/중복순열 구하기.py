#중복순열 구하기

#1, 2, 3 중에서 하나를 고르는 행위를 2번까지 하고 다시 돌아간다(O, X 아님) 
def DFS(L):
    global cnt
    if L == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            a[L] = i
            DFS(L+1)

n, m = map(int, input().split())

a = [0] * m
cnt = 0
DFS(0)
print(cnt)