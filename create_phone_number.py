def create_phone_number(n):
    result = "("
    i = 0
    for number in n:
        if(i == 3):
            result += ") " + str(number)
        elif(i == 6):
            result += "-" + str(number)
        else:
            result += str(number)
        i = i + 1
    return result

    
test = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
result = create_phone_number(test)
print(result)                


# return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)