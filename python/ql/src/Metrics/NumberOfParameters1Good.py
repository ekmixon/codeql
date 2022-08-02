class Annotation:
    #...
    pass

def print_annotation(annotation):
    print(f"Message: {annotation.message}")
    print(f"Line: {annotation.line}")
    print(f"Offset: {annotation.offset}")
    print(f"Length: {annotation.length}")
