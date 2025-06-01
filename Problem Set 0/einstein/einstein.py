"""
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

https://cs50.harvard.edu/python/psets/0/einstein/
"""

def main():
    m = int(input("Please enter a number representing mass in kilograms: "))
    c_squared = pow(300000000, 2)
    print("E =", m * c_squared)

if __name__ == "__main__":
    main()
