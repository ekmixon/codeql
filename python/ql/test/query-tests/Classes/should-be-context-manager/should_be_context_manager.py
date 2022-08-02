#Should be context manager

class MegaDel(object):

    def __del__(self):
        if a := self.x + self.y:
            print(a)
        if sys._getframe().f_lineno > 100:
            print("Hello")
        sum = 0
        for a in range(100):
            sum += a
        print(sum)

class MiniDel(object):

    def close(self):
        pass

    def __del__(self):
        self.close()