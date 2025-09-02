import re

def alphanumeric(password: str) -> bool:
    pattern = r"^[a-zA-Z0-9]+$"
    return True if re.fullmatch(pattern, password) else False



print(alphanumeric("Hello"))


# return string.isalnum()