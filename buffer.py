class Buffer:
    def __init__(self,size,initalvalue=0):
        self.size = size
        self.buffer = [initalvalue for _ in range(size)]
    def get(self,index):
        return self.buffer[index]
    def push(self,value):
        self.buffer.insert(0,value)
        self.buffer.pop()
    def top(self):
        return self.buffer[self.size-1]
    def list(self):
        return self.buffer