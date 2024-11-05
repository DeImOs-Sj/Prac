def fib(n):
    prev = 0
    next = 1
    stepc = 0
    for i in range(n):
        stepc += 1
        print(prev)
        temp = next
        next = prev + next
        prev = temp 
    print(f"step c = {stepc}")
fib(10)

# --------------------------

def fibRecr(n):
    if n <= 1:
        return n
    else:
        
        return fibRecr(n-1) + fibRecr(n-2)

n = 10
for i in range(n):
    print(fibRecr(i))