password = [[0,0,0,1,1,0,1], [0,0,1,1,0,0,1], [0,0,1,0,0,1,1], [0,1,1,1,1,0,1], [0,1,0,0,0,1,1], [0,1,1,0,0,0,1], [0,1,0,1,1,1,1], [0,1,1,1,0,1,1], [0,1,1,0,1,1,1], [0,0,0,1,0,1,1]]
tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    def psw():
        for i in range(n-5):
            for j in range(m-56):
                temp = True
                for k in range(j, j+56, 7):
                    if graph[i][k:k+7] in password:
                        continue
                    else:
                        temp = False
                if temp:
                    if graph[i][j:j+7] == graph[i+1][j:j+7] == graph[i+2][j:j+7] == graph[i+3][j:j+7] == graph[i+4][j:j+7]:
                        even = password.index(graph[i][j:j+7]) + password.index(graph[i][j+14:j+21]) + password.index(graph[i][j+28:j+35]) + password.index(graph[i][j+42:j+49])
                        odd = password.index(graph[i][j+7:j+14]) + password.index(graph[i][j+21:j+28]) + password.index(graph[i][j+35:j+42]) + password.index(graph[i][j+49:j+56])
                        
                        if (even*3 + odd) % 10 == 0:
                            return odd+even
        return 0
    print(f'#{t} {psw()}')