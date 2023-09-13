def square_numbers_and_return_sum(numbers):
    sum_of_squares = 0
    for num in numbers:
        squared_num = num ** 2
        sum_of_squares += squared_num
    return sum_of_squares
numbers = [1,3,5]
result = square_numbers_and_return_sum(numbers)
print(result)
