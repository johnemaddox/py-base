import unittest

from src.constants import *
from src.hello_world import HelloWorld

class Test_HelloWorld(unittest.TestCase):

    def setUp (self):
        self.hw = HelloWorld(HELLO_WORLD)

    def test_get_msg(self):
        '''
        get_msg() should return 'Hello, world!'.
        '''
        self.assertEqual(self.hw.get_msg(), HELLO_WORLD)


if __name__ == '__main__':
    unittest.main()
