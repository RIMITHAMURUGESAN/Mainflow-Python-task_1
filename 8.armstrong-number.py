def is_armstrong_number(n):
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return n == sum(d ** length for d in digits)

# Example usage:
print(is_armstrong_number(153))  # Output: True