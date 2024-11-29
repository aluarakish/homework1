def numbers(first: int, second: int, third: int, forth: int) -> int: 
    return max(first, second, third, forth)

result = numbers(10, 25, 7, 15)
print(f"Максимальное число: {result}")