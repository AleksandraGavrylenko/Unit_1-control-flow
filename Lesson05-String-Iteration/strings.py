# String Indexing
word = "Python"
#       012345 (positive indexing)
#      -654321 (negative indexing)
word[0]  # P
word[1]  # y
word[5]  # n
word[-1]  # n
len(word)  # length of string
word[len(word) - 1]  # n
# and Slicing
word[0:3]  # Pyt (char 0,1,2)
word[:3]  # same thing
word[2:5]  # tho (char 2,3,4)

word[2:6]  # thon (char 2,3,4,5)
word[2 : (len(word))]  # thon (char 2,3,4,5)
word[2:]  # thon (char 2,3,4,5)

word[-3:]  # hon (last 3 chars, -3,-2,-1 or 3,4,5)


# part1- string interation patterns
# direct char iteration
word = "Hello"

for char in word:
    print(char)

# index based iteration
for i in range(len(word)):
    print(f"Character {i}: {word[i]}")

# char classification
char = input("press one key")
# check char types using ASCII ranges
if "A" <= char <= "Z":
    print(f"{char} is uppercase")

if "a" <= char <= "z":
    print(f"{char} is lowercase")

if "0" <= char <= "9":
    print(f"{char} is a digit")

if "A" <= char <= "Z" or "a" <= char <= "z":
    print(f"{char} is a letter")
