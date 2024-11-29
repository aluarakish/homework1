def line(length: int, direction: str, symbol: str):
    if direction=='horizontal':
        print(symbol * length)
    elif direction=='vertical':
        for _ in range(length): 
            print(symbol)

line(10, 'horizontal', '*')

line(5, 'vertical', '#')