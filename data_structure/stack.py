from data_structure.node import Node


class Stack:
    def __init__(self):
        self.head = Node()

    def is_empty(self):
        return self.head.next is None

    def push(self, element):
        self.head.next = Node(element, self.head.next)

    def pop(self):
        node = self.head.next
        if not self.is_empty():
            self.head.next = node.next
        return node


def test():
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print('\n')
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == '__main__':
    # 运行测试函数
    test()