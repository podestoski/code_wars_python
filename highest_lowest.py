def high_and_low(numbers):
        numbers_int = numbers.split()
        highest = int(numbers_int[0])
        lowest = int(numbers_int[0])
        for number in numbers_int:
            if int(number) > highest:
                  highest = int(number)
            if int(number) < lowest:
                  lowest = int(number)
        return str(highest) + " " + str(lowest)


print(high_and_low("1 2 -3 4 5"))

# def high_and_low(numbers): #z.
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))