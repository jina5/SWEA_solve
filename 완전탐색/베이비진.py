def solve(card):
    new=[]
    for c in card:
        new.append(c)
        if len(new)<3:
            continue
        else:
            if search(new):
                return len(new)
    return 0

def search(card):
    n=len(card)
    card.sort()
    for i in range(n-2):
        if card[i]==card[i+1]==card[i+2]:
            return True
        elif card[i]+1 in card and card[i]+2 in card:
            return True

T=int(input())
for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    p1=arr[::2]
    p2=arr[1::2]
    p1=solve(p1)
    p2=solve(p2)
    if p1==0 and p2==0:
        result=0
    elif p1!=0 and p2==0:
        result=1
    elif p2!=0 and p1==0:
        result=2
    elif p1<p2:
        result=1
    elif p1==p2:
        result=1
    else:
        result=2
    print(f'#{tc} {result}')