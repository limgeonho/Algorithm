#이진트리순회(전위순회)

def DFS(x):
    if x > 7:
        return
    else:
        print(x, end='')
        DFS(x*2)
        DFS(x*2+1)
            
DFS(1)
