#부분집합구하기
'''
def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

n = int(input())
ch = [0] * (n+1)
DFS(1)
'''

def DFS(L, G):
    if L == n+1:
        print(G)
    else: 
        DFS(L+1, G+a[L])
        DFS(L+1, G)


n = int(input())
a = list(map(str, input().split()))
G = []
DFS(0, G)