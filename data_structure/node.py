class Node:
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)


"""
定义3个函数
append 添加一个元素到末尾
prepend 添加一个元素到开头
pop 删除并返回末尾的元素

prepend + pop 实现队列的入队（enqueue）和出队（dequeue）操作
append + pop 实现栈的入栈（push）和出栈（pop）操作
"""
