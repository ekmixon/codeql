# FP Reported in https://github.com/github/codeql/issues/2650

def possibly_unknown_format_string1(x):
    fmt = user_specified if (user_specified := unknown_function()) else "{a}"
    return fmt.format(a=1,b=2)

def possibly_unknown_format_string2(x):
    fmt = user_specified if (user_specified := input()) else "{a}"
    return fmt.format(a=1,b=2)


def possibly_unknown_format_string3(x):
    fmt = input() if unknown_function() else "{a}"
    return fmt.format(a=1,b=2)
