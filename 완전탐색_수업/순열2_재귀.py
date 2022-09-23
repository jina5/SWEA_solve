def f(i, k):
    if i == k:                      # i == 원소의 갯수 가 되었을 때 출력
        print(p)

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]


N = 10
p = [i for i in range(1, N+1)]
f(0, N)
