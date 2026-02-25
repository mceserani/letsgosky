print("Hello world!")

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    result = add(2, 3)
    print(f"The result of adding 2 and 3 is: {result}")

    result = mul(2, 3)
    print(f"The result of multiplying 2 and 3 is: {result}")

    try:
        result = divide(6, 2)
        print(f"The result of dividing 6 by 2 is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

    print("This is a test file for demonstrating code completion.")