def bi(n):
    if n//2==0:
        return str(n%2)
    else:
        return bi(n//2)+str(n%2)
