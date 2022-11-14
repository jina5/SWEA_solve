N = 10
for i in range(N-1):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(i, j, k)
