
def built_in_functions_max(num1, num2, num3):
    maxnum = max(num1, num2, num3)
    return maxnum



def built_in_functions_min(num1, num2, num3):
    minnum = min(num1, num2, num3)
    return minnum



def check_number(number):
    if number == 0:
        number = "Zero"
    elif number > 0:
        number = "Positive"
    elif number < 0:
        number = "Negative"
    return number



def star_shape(rows):
    star = ""
    for x in range(1, rows + 1):
        star += x * "*" + "\n"
    return star.rstrip()



def count_multiples_of_3(limit):
    number = ""
    i = 1
    while i <= limit:
        if i % 3 == 0:
            number += "Multiple of 3"
        else:
            number += str(i)
        i += 1
        number = str(number) + "\n"
    return number.rstrip()

print(count_multiples_of_3(20))



def sum_of_even_numbers(start, end):
    i = start
    sum = 0
    while i <= end:
        if i % 2 == 0:
            sum += i
            i += 1
        else:
            i += 1
            continue
    return sum

