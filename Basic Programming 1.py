N,t = input().split()
N = int(N) # N
t = int(t) # t
A = list(map(int,input().split())) # Array A with N integers
if t == 1: # print 7 regardless of A
    print(7) 
elif t == 2: # print whether A[0] is bigger, equal, or smaller versus A[1]
    if A[0] > A[1]:
        print('Bigger')
    elif A[0] == A[1]:
        print('Equal')
    else:
        print('Smaller')
elif t == 3: # print median of first 3 integers in A
    print(sorted(A[0:3])[1])
elif t == 4: # print sum of all integers in A
    print(sum(A))
elif t == 5: # print sum of all even integers in A
    print(sum(list(filter(lambda x: x%2 == 0, A))))
elif t == 6: # print A's elements mapped to alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print("".join(alphabet[i%26] for i in A))
else: # t = 7
    current_index_tortoise, current_index_hare = 0, 0 # initialize start index
    while True: 
        try:
            next_index_tortoise = A[current_index_tortoise]
            next_index_hare = A[A[current_index_hare]]
        except IndexError:
            print('Out')
            break
        if next_index_tortoise == N - 1 or next_index_hare == N - 1:
            print('Done')
            break
        elif next_index_hare == next_index_tortoise:
            print('Cyclic')
            break
        current_index_tortoise, current_index_hare = next_index_tortoise, next_index_hare
