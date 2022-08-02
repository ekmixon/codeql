import re
matcher = re.compile(r'(P<name>[\w]+)')

def only_letters(text):
    if m := matcher.match(text):
        print("Letters are: " + m.group('name'))

#Fix the pattern by adding the missing '?'
fixed_matcher = re.compile(r'(?P<name>[\w]+)')