def is_lucky_number(n: int) -> bool:
    if n < 100000 or n > 999999:
        return False
    n_str = str(n)
    sum_first_three = int(n_str[0]) + int(n_str[1]) + int(n_str[2])
    sum_last_three = int(n_str[3]) + int(n_str[4]) + int(n_str[5])
    return sum_first_three == sum_last_three

print(is_lucky_number(123420))
print(is_lucky_number(723422))

