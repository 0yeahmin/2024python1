def min_max(*numbers):
    min_value=numbers[0]
    max_value=numbers[0]
    for number in numbers:
        if min_value>number:
            min_value=number
        if max_value<number:
            max_value=number
    return min_value ,max_value

min, max=min_max(67,34,23,89,44)
print(min, max)