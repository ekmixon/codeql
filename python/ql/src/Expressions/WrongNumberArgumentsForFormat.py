def unsafe_format():
    args = (1, 2) if unlikely_condition() else (1, 2, 3)
    return "%s %s %s" % args
