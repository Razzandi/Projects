#! /usr/bin/env python3

class MyStack:
    def __init__(self,initial_values=None):
        if initial_values is None:
            initial_values = []
        self.theStack = initial_values

    def push(self,value):
        self.theStack.append(value)
        print(f"Pushed {value} onto the stack.")
    
    def pop(self):
        if self.theStack:
            return self.theStack.pop()
        return None
    
    def max(self):
        if self.theStack:
            return max(self.theStack)
        return None

# Demonstrate each of the functions in a main method
# Create stack with 5 random values between 0-100
def main():
    import random
    initial_values = [random.randint(0,100) for _ in range(5)]
    stack = MyStack(initial_values)
    print("Initial stack:", stack.theStack)

# Demonstrate push
    print("\nBefore push:", stack.theStack)
    stack.push(42)
    print("After push:", stack.theStack)

# Demonstrate pop
    print("\nBefore pop:", stack.theStack)
    popped = stack.pop()
    print("Popped value:", popped)
    print("After pop:", stack.theStack)

# Demonstrate max
    print("\nCurrent stack:", stack.theStack)
    max_value = stack.max()
    print("Max value:", max_value)


if __name__ == "__main__":
    main()