"""
In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You're welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

https://cs50.harvard.edu/python/psets/0/indoor/
"""

def main():
    user_text = input("Please enter text: ")
    print(user_text.lower())

if __name__ == "__main__":
    main()
