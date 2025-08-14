def solution(s):
    i = 0
    if len(s) % 2 != 0:
        s = s + "_"
    result_array = []
    temp_s = ""
    for c in s:
        if i == 0:
            temp_s = c
            i = i+1
        else:
            temp_s = temp_s + c
            i = 0
            result_array.append(temp_s)
    return result_array



print(solution("asdfadsf"))


# def solution(s):
#     result = []
#     if len(s) % 2:
#         s += '_'
#     for i in range(0, len(s), 2):
#         result.append(s[i:i+2])
#     return result
        