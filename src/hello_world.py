'''
Hello World

Use this as a template.

@author John E Maddox

'''

class HelloWorld ():
    '''
    Hello world example
    '''

    def __init__ (self, _msg):
        self.msg = _msg


    def get_msg (self):
        '''
        Return the message set in init.
        '''
        return self.msg


if __name__ == "__main__":
    hw = Hello_world('Test')
    print(hw.get_msg())
