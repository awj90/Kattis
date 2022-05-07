import sys

def bracket_type_check(stack, push): # returns True if stack and push are compatible open and close brackets
    if stack == '(' and push == ')':
        return True
    elif stack == '[' and push == ']':
        return True
    elif stack == '{' and push == '}':
        return True
    else:
        return False

len_L = int(input())
L = input()

stack = [''] # initialize

for i in range(len_L):
    if L[i] == ' ': continue # skip
    if L[i] == '(' or L[i] == '[' or L[i] == '{':
        stack.append(L[i]) # open brackets are ok
    elif not bracket_type_check(stack[-1],L[i]): # parenthesis error
        print(L[i], i)
        sys.exit()
    else:
        stack.pop()

print('ok so far')
    
