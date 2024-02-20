'''
# time exceed error
class Queue:
    def __init__(self):
        self.stack = []
        self.temp_stack = []
    
    def __len__(self):
        return len(self.stack)
    
    def enqueue(self, item):    
        self.stack.append(item)
        # print(self.stack)

    def dequeue(self):
        iter = self.__len__() - 1
        for _ in range(iter):
            self.temp_stack.append(self.stack.pop())
        self.stack.pop()
        for _ in range(iter):
            self.stack.append(self.temp_stack.pop())
        # print(self.stack)

    def printFront(self):
        print(self.stack[0])
'''
# trading space for time
class Queue:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []
    
    def __len__(self):
        
        return len(self.stack_enqueue)-len(self.stack_dequeue)
    
    def enqueue(self, item):  
        self.stack_enqueue.append(item)

    def dequeue(self):
        self.stack_dequeue.append(self.stack_enqueue[-1])

    def printFront(self):
        print(self.stack_enqueue[len(self.stack_dequeue)])
        

if __name__ == '__main__':

    queue = Queue()

    q = int(input())

    for _ in range(q):
        
        operation = list(map(int, input().rstrip().split()))

        match operation[0]:
            case 1:
                queue.enqueue(operation[1])
            case 2:
                queue.dequeue()
            case 3:
                queue.printFront()
            


        