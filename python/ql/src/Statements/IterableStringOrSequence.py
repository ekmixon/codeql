
#Mistakenly mixed list and string
def greeting():
    greet = [ "Hello", "World" ] if is_global() else "Hello"
    for word in greet:
        print(word)

#Only use list
def fixed_greeting():
    greet = [ "Hello", "World" ] if is_global() else [ "Hello" ]
    for word in greet:
        print(word)
