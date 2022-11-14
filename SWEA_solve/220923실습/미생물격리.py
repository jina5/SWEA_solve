di=[0,-1,1,0,0] #상하좌우(1234)
dj=[0,0,0,-1,1]
def move():
    for index in range(k):
        i,j,num,d=micros[index][0],micros[index][1],micros[index][2],micros[index][3]
        if num!=0:
            ni=i+di[d]
            nj=j+dj[d]
            if ni<1 or nj<1 or ni>n-2 or nj>n-2:
                num=num//2
                if d==1 or d==2:
                    d=d%2+1
                elif d==3 or d==4:
                    d=d%2+3
            micros[index]=[ni,nj,num,d]
    for i in range(k):
        if micros[i][2]!=0:
            temp=[]      
            for j in range(k):
                if i!=j:
                    if micros[i][0]==micros[j][0] and micros[i][1]== micros[j][1] and micros[j][2]!=0:
                        if micros[j] not in temp:
                            temp.append(micros[j])
            if temp:   
                temp.append(micros[i])
                max_num=temp[0][2]
                temp_i=0
                for i in range(len(temp)):
                    if temp[i][2]>max_num:
                        max_num=temp[i][2]
                        temp_i=i
                max_index=micros.index(temp[temp_i])
                temp.remove(temp[temp_i])
                for t in temp:
                    micros[max_index][2]+=t[2]
                    micros[micros.index(t)][2]=0
            
T=int(input())
for tc in range(1,T+1):
    n,m,k=map(int,input().split())
    micros=list(list(map(int,input().split())) for _ in range(k))
    for _ in range(m):
        move()
    result=0
    for micro in micros:
        result+=micro[2]
    print(f'#{tc} {result}')
    