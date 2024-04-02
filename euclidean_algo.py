
"""
PSEUDO CODE 

function extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


"""

# Implementation of EuclideanAlgorithm
class EuclideanAlgorithm:
    @staticmethod
    def extended_gcd(a, b):
        # Base case: if b is zero, return a as the GCD, and coefficients x=1, y=0
        if b == 0:
            return a, 1, 0
        else:
            # Recursive step: recursively call the function with b and a mod b
            gcd, x1, y1 = EuclideanAlgorithm.extended_gcd(b, a % b)
            # Calculate coefficients x and y
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y

if __name__ == "__main__":
    try:
        # Take input from the user for two positive integers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        # Check if the input is valid
        if num1 <= 0 or num2 <= 0:
            raise ValueError("Numbers should be positive integers")

        # Call the extended_gcd method to compute the GCD and coefficients
        gcd, x, y = EuclideanAlgorithm.extended_gcd(num1, num2)
        
        # Print the GCD and coefficients along with the equation representing the GCD
        print(f"GCD of {num1} and {num2} is {gcd}")
        print(f"Coefficients (x, y): ({x}, {y})")
        print(f"{x}*{num1} + {y}*{num2} = {gcd}")
    except ValueError as ve:
        # Print error message if input is invalid
        print("Error:", ve)
