#조합 구하기

#순열과 비슷하게 DFS(O, X)아님 + 하나씩 선택을 하되, 선택 시작수를 +1씩 증가시켜줘야함
def DFS(L, s):
    global cnt
    if L == m:
        for x in a:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n+1):
            a[L] = i
            DFS(L+1, i+1)

n, m = map(int, input().split())
cnt = 0
a = [0] * m
DFS(0, 1)
print(cnt)