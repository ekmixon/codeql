s = "taintedString"

sw = s.startswith
if sw("safe"):  # $ MISSING: checks=s branch=true
    pass
