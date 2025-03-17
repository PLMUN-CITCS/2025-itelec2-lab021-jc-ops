"""Gets a number and finds factorial."""
def get_non_negative_integer():
    """Gets a non-negative integer."""
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Must not be negative.")
                continue
            return num
        except ValueError:
            print("Must be an integer.")

def calculate_factorial(n):
    """Finds factorial of a number."""
    if n == 0:
        result = 1
    else:
        result = n * calculate_factorial(n - 1)
    return result

if __name__ == "__main__":
    print(calculate_factorial(get_non_negative_integer()))
