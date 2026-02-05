#   * * * * * * 
#   *         *
#   *         *
#   *         *
#   *         *
#   * * * * * * 
rows = int(input())

# Top row
for j in range(rows):
    print("*", end=" ")
print()

# Middle rows
for i in range(rows - 2):
    print("*", end=" ")
    for j in range(rows - 2):
        print(" ", end=" ")
    print("*")

# Bottom row
for j in range(rows):
    print("*", end=" ")
