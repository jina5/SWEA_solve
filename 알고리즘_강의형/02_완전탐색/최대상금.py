def dfs(cnt, n):
    global answer
    if cnt == n :
        temp = int(''.join(num))
        if answer < temp :
            answer = temp
        return
    for i in range(l-1):
        for j in range(i+1,l):
            num[i], num[j] = num[j], num[i]
            temp = int(''.join(num))
            if (cnt,temp) not in check:
                check.append((cnt,temp))
                dfs(cnt+1,n)
            num[i], num[j] = num[j], num[i]
    
for tc in range(1,int(input())+1):
    num, n = input().split()
    n = int(n)
    num= list(num)
    l = len(num)
    check=[]
    answer = 0
    dfs(0,n)
    print(f'#{tc} {answer}')
