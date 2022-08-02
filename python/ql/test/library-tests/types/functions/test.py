import zope.interface

#ODASA-6062
class Z(zope.interface.Interface):

    def yes(self):
        pass

class NotZ(object):

    def no(self):
        pass
