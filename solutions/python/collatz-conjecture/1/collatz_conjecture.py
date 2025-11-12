def steps(number):
    steps = 0
    
    while number != 1:
        if number <= 0:
            raise ValueError("Only positive integers are allowed")

        if number % 2 == 0:
            number //= 2
        elif number % 2 == 1:
            number *= 3
            number += 1

        steps += 1

    return steps