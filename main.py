import common.constants as const
from HelloWorld import HelloWorld

def main ():

  hw = HelloWorld(const.HELLO_WORLD)
  print(hw.getMsg())
  

if __name__ == '__main__':
  main()
  