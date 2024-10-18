def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if fib_sequence[-1] > n:
        fib_sequence.pop()
    return fib_sequence
print(fibonacci(10)) 
print(fibonacci(5))   
def generate_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
print(list(generate_fibonacci(10))) 