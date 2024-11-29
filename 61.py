def print_odd_numbers(start: int, end: int):
    current = start + 1
   
    while current < end:
        if current % 2 != 0: 
            print(current)
        current += 1  


print_odd_numbers(5, 15)
