# palindrome.py

text = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
