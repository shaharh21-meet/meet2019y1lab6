
def add_numbers(start, end):
    
    total = 0
    for number in range(start, end + 1):
        total = total + number
        print(total)
    return total
    
answer = add_numbers(333,777)
print(answer)

