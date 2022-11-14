def dfs(cnt, n):
    global answer
    if cnt == n :
        temp = ''.join(num)
        temp = int(temp)
        if answer < temp :
            answer = temp
        return
    for i in range(l-1):
        for j in range(i+1,l):
            num[i], num[j] = num[j], num[i]
            temp = ''.join(num)
            temp= int(temp)
            if visited.get((temp,cnt),0)==0:
                visited[(temp,cnt)]=1
                dfs(cnt+1,n)
            num[i], num[j] = num[j], num[i]

    
    
for tc in range(1,int(input())+1):
    num, n = input().split()
    n = int(n)
    num= list(num)
    l = len(num)
    visited = {}
    answer = 0
    dfs(0,n)
    print(f'#{tc} {answer}')
