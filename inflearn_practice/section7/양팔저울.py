#양팔저울

#추의 무게를 선택할지 안할지(O, X) 
# + 반대로 빼는 부분을 추가해서 저울의 반대편에 놓는 방법 추가(O, X)
def DFS(L, sum):
    global res
    if L == n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+g[L])
        DFS(L+1, sum-g[L])
        DFS(L+1, sum)
n = int(input())
g = list(map(int, input().split()))
s = sum(g)
res = set()
DFS(0, 0)
print(s - len(res))