import re

def IsEmail(text: str) -> bool:
    return bool(re.findall(r"[\w+\.-]+@\w+\.\w{3}",text))

def IsPhone(text: str) -> bool:
    return bool(re.findall(r"0\d{9}", text))
