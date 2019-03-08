length=0
visited=[]
def Highest(Map):
    Max=0
    temp=[]
    for i in range(len(Map)):
        for j in range(len(Map)):
    	    if Map[i][j]>Max: Max,temp=Map[i][j],[]
    	    if Map[i][j]==Max: temp.append([i,j])
    return temp

def moving(start,Map,Flag):
    global length
    if len(visited)>length:
        length=len(visited)
        #print(visited)
    L=len(Map)
    R=Map[start[0]][start[1]]
    for _ in range(4):
        if _==0: step=[start[0]+1,start[1]]
        if _==1: step=[start[0]-1,start[1]]
        if _==2: step=[start[0],start[1]+1]
        if _==3: step=[start[0],start[1]-1]
        if L>step[0]>-1 and L>step[1]>-1 and R>Map[step[0]][step[1]] and step not in visited: 
            visited.append(step)
            moving(step,Map,Flag)
            visited.pop()
        elif L>step[0]>-1 and L>step[1]>-1 and R>Map[step[0]][step[1]]-K and step not in visited and Flag: 
            visited.append(step)
            X=Map[step[0]][step[1]]
            Map[step[0]][step[1]]=R-1
            moving(step,Map,False)
            Map[step[0]][step[1]]=X
            visited.pop()

T=int(input())

for test_case in range(1,T+1):
    print("#",end="")
    print(test_case,end=" ")
    N,K=map(int,input().split())
    Map=[[] for i in range(N)]
    for i in range(N): Map[i]=list(map(int,input().split()))
    High=Highest(Map)
    
    answer=[]
    length=0
    for start in High:
        visited.append(start)
        moving(start,Map,True)
        answer.append(length)
        visited.pop()
    print(max(answer))
