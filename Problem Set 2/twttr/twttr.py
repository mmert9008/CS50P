"""
When texting or tweeting, it's not uncommon to shorten words to save time or
space, as by omitting vowels, much like Twitter was originally called twttr.
In a file called twttr.py, implement a program that prompts the user for a
str of text and then outputs that same text but with all vowels (A, E, I, O,
and U) omitted, whether inputted in uppercase or lowercase.

https://cs50.harvard.edu/python/2022/psets/2/twttr/
"""


def main() -> None:
    user_input = input("Input: ")
    shortened_input = ""
    for char in user_input:
        if char not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            shortened_input += char
    print(f"Output: {shortened_input}")


if __name__ == "__main__":
    main()
