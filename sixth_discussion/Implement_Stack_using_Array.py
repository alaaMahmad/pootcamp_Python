class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []  
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, element):
        if self.is_full():
            print("Stack Overflow")
            return
        
        self.top += 1
        self.arr.append(element)
        print(f"Pushed {element} to stack.")

    def pop(self):
        if self.is_empty():
            return print("Stack Underflow")

        popped_val = self.arr.pop()
        self.top -= 1
        return popped_val

    def peek(self):
        if self.is_empty():
            return print("Stack is empty")      
        return self.arr[self.top]



my_stack = Stack(3)

print("Push Operations")
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

my_stack.push(40) 

print("\nPeek Operation")
print("Top element is:", my_stack.peek())

print("\nPop Operations")
print("Popped element:", my_stack.pop())
print("Popped element:", my_stack.pop())
print("Popped element:", my_stack.pop())
    
print("Popped element:", my_stack.pop())


