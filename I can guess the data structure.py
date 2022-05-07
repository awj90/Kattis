from collections import deque

while True:

    try: 
        n = int(input()) # number of test cases 1 <= n <= 1000

        # initialization
        is_stack = True
        is_queue = True
        is_priorityqueue = True
        is_impossible = False
        stack_bag = []
        queue_bag = deque([])
        priorityqueue_bag = []

        for i in range(n):
            operation, x = input().split()
            operation = int(operation) # 1: add element, 2: remove element
            x = int(x) # positive integer not larger than 100

            if operation == 1: # add element to bag
                stack_bag.append(x)
                queue_bag.append(x)
                priorityqueue_bag.append(x)
                    
            else: # remove element from bag

                if (x not in stack_bag) and (x not in queue_bag) and (x not in priorityqueue_bag):
                    # none of stack, queue, or priority queues would remove an element not in the bag
                    is_impossible = True
                
                else:

                # check if it could be a stack
                    if x != stack_bag.pop(): # definitely not stack if x was not the last-in element
                        is_stack = False

                #check if it could be a queue
                    if x != queue_bag.popleft(): # definitely not queue if x was not the first-in element
                        is_queue = False

                # check if it could be a priority queue
                    if x != max(priorityqueue_bag): # definitely not priority queue if x was not the largest in the bag
                        is_priorityqueue = False
                    if x == max(priorityqueue_bag):
                        priorityqueue_bag.remove(x) # dequeue x which has highest priority

        # print outputs after checking
        if is_impossible:
            print('impossible')
        elif (not is_stack) and (not is_queue) and (not is_priorityqueue): # also impossible
            print('impossible')
        elif (is_stack + is_queue + is_priorityqueue) > 1: # not conclusive
            print('not sure')
        elif is_stack:
            print('stack')
        elif is_queue:
            print('queue')
        elif is_priorityqueue:
            print('priority queue')        

    except EOFError: # EOF break for input()
        break
    except ValueError: # ValueError break for int(input())
        break
