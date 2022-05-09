class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return bool(self.elements)

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        self.elements.pop()
        return self.elements[-1]

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)


stack = Stack()
stack.push('cat')
stack.push(3)
stack.push('554')
stack.push(1.2)
print(stack.size())
