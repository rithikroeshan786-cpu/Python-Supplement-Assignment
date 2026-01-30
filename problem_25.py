# Problem 25: Find GCD of two numbers
# Find and fix the error

def gcd(a, b):
    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)
    
    while b != 0:
        a, b = b, a % b  # Swap a and b
    return a

print(f"GCD of 48 and 18: {gcd(48, 18)}")
