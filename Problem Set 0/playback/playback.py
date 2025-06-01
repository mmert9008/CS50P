"""
In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

https://cs50.harvard.edu/python/psets/0/playback/
"""

def main():
    user_text = input("Please enter text: ")
    print(user_text.replace(" ", "..."))

if __name__ == "__main__":
    main()
