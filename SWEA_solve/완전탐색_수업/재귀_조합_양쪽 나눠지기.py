an = []  # n개 원소 가지고 있는 배열
tr = []  # r개 크기의 배열, 조합이 임시 저장될 배열


def comb(n, r):
    if r == 0:
        print(tr)
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)
