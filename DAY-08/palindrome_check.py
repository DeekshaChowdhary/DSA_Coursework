#------- PALINDROME CHECK------------


# USING STRING REVERSAL
text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# USING TWO POINTERS
def is_palindrome(string):
    string = string.lower()
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True


text = input("\nEnter another word: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
