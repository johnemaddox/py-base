import unittest

import common.constants as const
from HelloWorld import HelloWorld

class Test_HelloWorld(unittest.TestCase):

  def setUp (self):
    self.hw = HelloWorld(const.HELLO_WORLD)


  def test_getMsg(self):
    '''
    getMsg() should return 'Hello, world!'.
    '''
    self.assertEqual(self.hw.getMsg(), const.HELLO_WORLD)


if __name__ == '__main__':
  unittest.main()
