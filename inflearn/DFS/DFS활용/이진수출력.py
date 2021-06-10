#이진수출력
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

n = input()
DFS(n)