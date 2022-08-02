from unittest import TestCase

class MyTest(TestCase):
    
    
    def testInts(self):
        self.assertTrue(True)
        self.assertFalse(1 > 2)
        self.assertTrue(1 in {})
