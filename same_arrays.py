def comp(array1, array2):
    # Validate that both arrays are different from None(null)
    # Explict == None, if not array will return true if len = 0
    if array1 == None or array2 == None:
        return False
    
    # Make array positives integer so the sorting makes sense
    array1 = [abs(number) for number in array1]
    array2 = [abs(number) for number in array2]
    
    # Sorting to match element by element. Meaning array2[0] == array1[0]^2
    array1.sort()
    array2.sort()

    # Printing to validate test cases
    print(array1)
    print(array2)

    # If the len of both arrays is not equal, therefore there is no need to validate squares. They don't have the same numbers of elements
    if(len(array1) != len(array2)):
        return False
    
    # Compare both elements
    for a1,a2 in zip(array1,array2):
        if(a2 != (a1*a1)):
            return False
    return True

a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a1, a2))


# if None in [array1, array2] or len(array1) != len(array2):
#         return False
    
#     for number in array1:

#         try:
#             array2.remove(number*number)
#         except ValueError:
#             return False
    
#     return True