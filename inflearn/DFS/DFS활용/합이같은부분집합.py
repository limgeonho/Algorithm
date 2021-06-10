#합이같은부분집합

def DFS(L, sum):
    if sum > total//2:
        return
    if L == n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

n = input()  
a = list(int, map(input().split()))
total = sum(a)
DFS(0, 0)
print("NO")
