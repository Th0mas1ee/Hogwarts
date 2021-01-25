from animal import Animal
from cat import Cat

if __name__ == '__main__':
    animal = Animal()
    animal.run()
    animal.shout()
    cat = Cat()
    print(f"Cat' name: {cat.name}, color: {cat.color}, hair: {cat.hair}")
    cat.run()
    cat.shout()


