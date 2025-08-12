def to_jaden_case(string):
    result = ""
    first = True
    for s in string.split(" "):
        if(first):
            result = s.capitalize()
            first = False
        else:
            result = result + " " + s.capitalize()
    return result

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))