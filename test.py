print("Hello world!")

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def power(a, b):
    return a ** b


def log2(a):
    import math
    return math.log2(a)
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    result = add(2, 3)
    print(f"The result of adding 2 and 3 is: {result}")

    result = mul(2, 3)
    print(f"The result of multiplying 2 and 3 is: {result}")

    print("This is a test file for demonstrating code completion.")