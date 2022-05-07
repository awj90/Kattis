import heapq

T = int(input()) # number of test cases

for i in range(T):
    N = int(input()) # number of canvasses
    canvass_sizes = list(map(int,input().split())) # list of canvass sizes
    heapq.heapify(canvass_sizes) # min heap 
    used_paint = 0 # initialize
    while len(canvass_sizes) >= 2:
        smallest = heapq.heappop(canvass_sizes) 
        second_smallest = heapq.heappop(canvass_sizes)
        used_paint = used_paint + smallest + second_smallest # accumulate used paint
        heapq.heappush(canvass_sizes, smallest + second_smallest)
    print(used_paint)
