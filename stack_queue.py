class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 

a=Stack()
b=Queue()
ch=0
while(ch!=7):
    print("1.pop op.in stack\n2.push op. in stack\n3.length of stack\n4.enqueue op.in queue\n5.dequeue op. in queue\n6.length of queue")
    ch=int(input())
    if(ch==1):
        a.pop()
        print(a.stack)
    if(ch==2):
        val=input("Enter value to push:")
        a.push(val)
        print(a.stack)
    if(ch==3):
        print(a.size())
    if(ch==4):
        num=input("enter the value to enqueue:")
        b.enqueue(num)
        print(b.queue)
    if(ch==5):
        b.dequeue()
        print(b.queue)
    if(ch==6):
        print(b.size())
    
