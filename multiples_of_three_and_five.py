def sum_of_multiples(num1, num2):
    
    r1, r2 = 0, 1000
    total = 0

    for i in range(r1, r2):
        if i % num1 == 0 or i % num2 == 0:  
            total += i
    return total
