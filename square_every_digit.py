def square_digits(num):
    num_str = str(num)
    result_str = ""
    for digit in num_str:
        square = int(digit) * int(digit)
        result_str = result_str + str(square)
    return int(result_str)

print(square_digits(9119))


# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)