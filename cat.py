from animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.hair = 'short hair'

    def catch(self):
        print('It is catching a mouse.')

    def shout(self):
        print('It is miaowing.')
