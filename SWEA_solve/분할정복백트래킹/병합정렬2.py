# l,r : 정렬 대상 인덱스
def merge_sort(l, r):
    if l == r:
        return
    m = (l+r)//2
    merge_sort(l, m)
    merge_sort(m+1, r)
    merge(l, r)
    

def merge(l, r):
    result = []
    m = (l+r)//2
    i = l
    j = m+1
    while i <= m and j <= r:
        if arr[i] < arr[j]:
            result.append(arr[i])
            i = i+1
        else:
            result.append(arr[j])
            j = j+1
    while j <= r:
        result.append(arr[j])
        j += 1
    while i <= m:
        result.append(arr[i])
        i += 1
    #arr에 result 요소 복사하기
    index=0
    for a in range(l,r+1):
        arr[a] = result[index]
        index+=1
    


arr = [2, 9, 3, 1, 4, 4, 7, 8, 11]
N = len(arr)
result=merge_sort(0, N-1)
print(arr)
