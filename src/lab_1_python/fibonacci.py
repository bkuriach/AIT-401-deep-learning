# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

class Fibonacci:
    def __init__(self):
        self.n = 0
        self.fibonacci = []
    def generate_fibonacci_series(self, n):
        self.n = n
        if self.n <= 0:
            print("Please enter a positive integer")
        elif self.n == 1:
            self.fibonacci.append(1)
        elif self.n == 2:
            self.fibonacci.append(0)
            self.fibonacci.append(1)
            return self.fibonacci
        else:
            self.fibonacci.append(0)
            self.fibonacci.append(1)
            for i in range(2, self.n):
                self.fibonacci.append(self.fibonacci[i-1] + self.fibonacci[i-2])
            return self.fibonacci

obj = Fibonacci()
obj.generate_fibonacci_series(10)