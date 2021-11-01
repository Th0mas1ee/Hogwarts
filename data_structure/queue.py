from data_structure.node import Node


class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def is_empty(self):
        return self.head.next is None

    def enqueue(self, element):
        node = Node(element)
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        node = self.head.next
        if not self.is_empty():
            self.head.next = node.next
        return node


def test():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print('\n')
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


if __name__ == '__main__':
    # 运行测试函数
    test()
