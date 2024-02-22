def sumFileNumbers(file):
    with open(file) as f:
        numbers = f.read()
    numbers = numbers.split('; ')

    sum = 0
    for i in numbers:
        number = int(i)
        if number <= 10 and number >= -10:
            sum += number
    return sum