class Spam:

    def __init__(self):
        self.spam = 'spam, spam, spam'

    def set_eggs(eggs):
        self.eggs = eggs

    def __str__(self):
        return f'{self.spam} and {self.eggs}'

#Fixed version

class Spam:

    def __init__(self):
        self.spam = 'spam, spam, spam'
        self.eggs = None

    def set_eggs(eggs):
        self.eggs = eggs

    def __str__(self):
        return f'{self.spam} and {self.eggs}'

