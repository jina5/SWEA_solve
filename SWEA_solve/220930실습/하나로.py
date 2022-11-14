def cost(x1,y1,x2,y2):
    global e
    result=((x1-x2)**2+(y1-y2)**2)**(1/2)
    result= e*(result**2)
    return result

def prim(r, n):
    MST = [0]*n    
    key = [1e9]*n
    key[r] = 0         
    for _ in range(n):  
        u = 0
        minV = 10000
        for i in range(n):
            if MST[i]==0 and key[i]<minV:
                u = i
                minV = key[i]
        MST[u] = 1                
        for v in range(n):
            if MST[v]==0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])  
    return sum(key)


T=int(input())
for tc in range(1,T+1):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    e=float(input())
    arr=[]
    adjM = [[0]*(n) for _ in range(n)]

    for i in range(n):
        arr.append((x[i],y[i]))
        
    for i in range(n):
        for j in range(n):
            if i!=j:
                adjM[i][j]=cost(arr[i][0],arr[i][1],arr[j][0],arr[j][1])
                adjM[j][i]=cost(arr[i][0],arr[i][1],arr[j][0],arr[j][1])
    
    print(prim(0,n))            

    