from animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.hair = 'short hair'

    def catch(self):
        print('Cat is catching a mouse.')

    def shout(self):
        print('Cat is miaowing.')
