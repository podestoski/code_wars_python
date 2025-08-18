def generate_hashtag(s):
    if(len(s) == 0):
        return False
    else:
        s = s.strip()
        s = to_camel_case(s)
        s = s.replace(" ", "")
        if(len(s) > 139):
            return False
        else:
            return "#" + s


def to_camel_case(s):
    components = s.split(' ')
    return components[0].title() + ''.join(x.title() for x in components[1:])
        

print (generate_hashtag("  a  bb  ccc  dddd  eeeee  ffffff  ggggggg  hhhhhhhh  iiiiiiiii  jjjjjjjjjj  kkkkkkkkkkk  llllllllllll  mmmmmmmmmmmmm  nnnnnnnnnnnnnn  ooooooooooooooo  pppppppppppppppp  qqq"))

# def generate_hashtag(s):
#     output = "#"
    
#     for word in s.split():
#         output += word.capitalize()
    
#     return False if (len(s) == 0 or len(output) > 140) else output
        