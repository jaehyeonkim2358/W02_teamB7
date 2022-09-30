

stack = [1, 2, 3]

# init
stack = []

# push
stack.append(4)

# pop
stack.pop()

# peek
top = stack[-1]

stack = []

def is_empty():
    stack

def push(n):
    stack.append(n)

def pop():
    if len(stack) == 0:
        return -1
    else:
        stack.pop()
        print(stack[-1])

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]