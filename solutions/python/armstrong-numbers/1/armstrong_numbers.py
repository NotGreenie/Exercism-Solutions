def is_armstrong_number(number):
    total = 0
    
    number_list = [int(digit) for digit in str(number)]

    digits = len(number_list)

    for digit in number_list:
        total += digit ** digits

    return True if total == number else False
