class Tree:
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def traversal(self):
        # print(self.element)
        if self.left is not None:
            self.left.traversal()
        print(self.element)
        if self.right is not None:
            self.right.traversal()
        # print(self.element)

    def reverse(self):
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()


def test():
    # 手动构建二叉树
    # 为什么手动这么麻烦呢, 因为一般都是自动生成的
    # 这里只需要掌握性质就好
    t = Tree(0)
    left = Tree(1)
    right = Tree(2)
    t.left = left
    t.right = right
    # 遍历
    print('\n')
    t.traversal()
    t.reverse()
    t.traversal()
    print('@@', [i * 3 for i in range(1, 4)])
    switch = 1
    do = 1
    print(switch) if switch == do else print(do)
    if switch == 1: print(switch)
    s = [1, 2, 3, 4, 5, 6]
    print("!!", s[1:4:2])



if __name__ == '__main__':
    test()

