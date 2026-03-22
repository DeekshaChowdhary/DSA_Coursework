#------- COUNTING PROGRAMS -----------------------


#1. EVEN & ODD COUNT (1 to n)
n = int(input("Enter a number: "))

even = 0
odd = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)


# 2. COUNT DIGITS
num = int(input("\nEnter a number: "))
count = 0

if num == 0:
    count = 1
else:
    num = abs(num)
    while num > 0:
        num //= 10
        count += 1

print("Digit count:", count)


# 3. COUNT PRIME NUMBERS
n = int(input("\nEnter a number: "))
prime_count = 0

for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1

print("Prime count:", prime_count)


# 4. COUNT VOWELS & CONSONANTS
text = input("\nEnter a string: ")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for ch in text:
    if ch in vowels:
        v_count += 1
    elif ch.isalpha():
        c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)


# 5. COUNT CHARACTER
text = input("\nEnter a string: ")
char = input("Enter character to count: ")

count = 0
for ch in text:
    if ch == char:
        count += 1

print(f"{char} appears:", count)


# 6. SUM OF DIGITS
num = int(input("\nEnter a number: "))
total = 0

num = abs(num)
while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits:", total)


# 7. REVERSE NUMBER
num = int(input("\nEnter a number: "))
rev = 0

num = abs(num)
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reversed number:", rev)


# 8. COUNT CHARACTERS IN STRING
text = input("\nEnter text: ")
count = 0

for ch in text:
    count += 1

print("Character count:", count)


# 9. COUNT VOWELS ONLY
text = input("\nEnter text: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)


# 10. REVERSE STRING
text = input("\nEnter text: ")
rev_text = ""

for ch in text:
    rev_text = ch + rev_text

print("Reversed text:", rev_text)


# 11. COUNT EVEN DIGITS IN NUMBER
num = int(input("\nEnter a number: "))
count = 0

for digit in str(num):
    if int(digit) % 2 == 0:
        count += 1

print("Even digits count:", count)
