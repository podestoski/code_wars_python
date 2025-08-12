def solution(text, ending):
    lenText = len(text)
    lenEnding = len(ending)
    for i in range(lenEnding):
        if(text[lenText - i - 1] != ending[lenEnding - i - 1]):
            return False
    return True



print (solution("ninja", "jb"))


# def solution(text, ending):
#     len_end = len(ending)
#     word = text[-len_end:]
#     if word == ending:
#         print('true')
#         return True
#     else:
#         print('false')
#         return False

# return string.endswith(ending)