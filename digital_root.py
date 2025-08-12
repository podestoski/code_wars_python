def digital_root(n):
    result = 0
    n_str = str(n)
    for number in n_str:
        result = result + int(number)
    result_length = len(str(result))
    if(result_length > 1):
        return digital_root(result)
    else:
        return result

print(digital_root(132189))