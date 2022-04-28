def validate(string):

    param = "(" + ")"
    if "def" not in string:
        return "missing def"
    if ":" not in string:
        return "missing :"
    if "(" and ")" not in string:
        return "missing paren"
    if param in string:
        return "missing param"
    if string.count(' ') < 4:
        return "missing indent"
    if "validate" not in string:
        return "wrong name"
    if "return" not in string:
        return "missing return"
    return True
