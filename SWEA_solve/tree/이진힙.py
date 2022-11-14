def minheap(v):
    global heap_count
    heap_count += 1
    heap[heap_count] = v
    child = heap_count
    parent = heap_count // 2
    while child  and heap[parent] > heap[child]:
        heap[parent], heap[child] =  heap[child], heap[parent]
        child = parent
        parent = child // 2
 
T = int(input())
 
for tc in range(1,T+1):
    N = int(input())
    heap = [0] * (N+1)
    heap_count = 0
    lst = list(map(int,input().split()))
    for i in lst:
        minheap(i)
 
    sum_heap = 0
    while heap_count > 0:
        heap_count  //=  2
        sum_heap += heap[(heap_count)]
 
 
    print(f'#{tc} {sum_heap}')