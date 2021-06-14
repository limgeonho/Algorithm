#순열구하기

#1, 2, 3 중에서 하나를 고르는 행위를 2번까지 하고 다시 돌아간다(O, X 아님)
#+ 중복된 항목을 점검하는 점에서 중복순열과 다름 
def DFS(L):
    global cnt
    if L == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                a[L] = i
                DFS(L+1)
                ch[i] = 0


n, m = map(int, input().split())
ch = [0] * (n+1)
a = [0] * m
cnt = 0

DFS(0)
print(cnt)