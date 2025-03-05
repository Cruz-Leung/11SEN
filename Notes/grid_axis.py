def draw_grid(n, x, y):
    for row in range(1, n * 2 + 2):
        if row % 2 == 1:  # Draw horizontal separators
            print("+" + "-+" * n)
        else:  # Draw vertical separators and the 'x'
            for col in range(1, n * 2 + 2):
                if col % 2 == 1:
                    print("|", end="")
                elif row // 2 == y and col // 2 == x:
                    print("x", end="")
                else:
                    print(" ", end="")
            print()  # Move to next row

# Get user input
n = int(input("n: "))
x = int(input("x: "))
y = int(input("y: "))

# Draw the grid
draw_grid(n, x, y)
