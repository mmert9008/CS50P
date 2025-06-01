"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file's media type if the file's name ends, case-insensitively, in any of these suffixes:
- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip

If the file's name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

https://cs50.harvard.edu/python/psets/1/extensions/
"""

def main():
    user_input = input("Enter a file name: ").strip().lower()
    if user_input.endswith(".gif"):
        print("image/gif")
    elif user_input.endswith(".jpg"):
        print("image/jpeg")
    elif user_input.endswith(".jpeg"):
        print("image/jpeg")
    elif user_input.endswith(".png"):
        print("image/png")
    elif user_input.endswith(".pdf"):
        print("application/pdf")
    elif user_input.endswith(".txt"):
        print("text/plain")
    elif user_input.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
