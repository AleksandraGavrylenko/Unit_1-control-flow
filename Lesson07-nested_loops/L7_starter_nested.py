#UNIT 2 - LESSON 7: NESTED LOOPS & PATTERN GENERATION
# PART 1: BASIC EXAMPLES - 1


# EXAMPLE-1- Basic Nested Loop Coordinates
# ======================================

# print("=" * 50)
# print("EXAMPLE 1: Basic Nested Loop Coordinates")
# print("=" * 50)

# for outer in range(3):
#     for inner in range(4):
#         print(f"({outer}, {inner})", end=" ")
#     print()  # New line after inner loop completes


# EXAMPLE-2- Rectangle of Stars
# ======================================


# print("\n" + "=" * 50)
# print("EXAMPLE 2: Rectangle")
# print("=" * 50)

# rows = 5
# cols = 8
# for i in range(rows):
#     for j in range(cols):
#         print("*", end="")
#     print()


# EXAMPLE-3- Right triangle
# ======================================


# print("\n" + "=" * 50)
# print("EXAMPLE 3: Right Triangle")
# print("=" * 50)

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()


# EXAMPLE-4- Number Triangle
# ======================================


# print("\n" + "=" * 50)
# print("EXAMPLE 4: Number Triangle")
# print("=" * 50)

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
    
    
# EXAMPLE-5- Multiplication Table (5x5)"
# ======================================

rows = 5
columns = 5
print("\n" + "=" * 50)
print(f"EXAMPLE 5: Multiplication Table ({rows}x{columns})")
print("=" * 50)
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        product = i * j
        print(f"{product:4}", end="")
    print()

