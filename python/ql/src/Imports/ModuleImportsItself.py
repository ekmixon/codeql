import ModuleImportsItself

def factorial(n):
    return 1 if n <= 0 else n * ModuleImportsItself.factorial(n - 1)