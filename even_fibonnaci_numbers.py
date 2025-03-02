# Problem 02: Even Fibonacci Numbers
# Link: https://projecteuler.net/problem=2 
# Formula: Fn = Fn-1 + Fn-2


def fibonnaci_numbers(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonnaci_numbers(n-1) + fibonnaci_numbers(n-2)
    
def sum_even_numbers(limit):
    total_sum = 0

    for i in range(limit):
        fib_num = fibonnaci_numbers(i)
        if fib_num % 2 == 0:
            total_sum += fib_num
    return total_sum

print(sum_even_numbers(50))