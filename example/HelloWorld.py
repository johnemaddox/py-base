
class HelloWorld ():
  '''
  Hello world example
  '''
  msg = None


  def __init__ (self, _msg):
    self.msg = _msg


  def getMsg (self):
    '''
    Return the message set in init.
    '''
    return self.msg


if __name__ == "__main__":
  hw = HelloWorld('Test')
  print(hw.getMsg())
