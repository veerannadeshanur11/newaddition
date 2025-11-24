import sys

def add(a, b):
    return a + b

def main():
    if len(sys.argv) != 3:
        print("Usage: python addition.py <num1> <num2>")
        sys.exit(1)

    try:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    except ValueError:
        print("Error: Inputs must be numbers.")
        sys.exit(1)

    print("Sum:", add(x, y))

if __name__ == "__main__":
    main()
