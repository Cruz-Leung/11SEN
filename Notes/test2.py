def draw_grid(n, x, y):
    for row in range(1, n * 2 + 2):
        if row % 2 == 1:  # Draw horizontal separators
            print("+ " + "- + " * (n - 1) + "+")
        else:  # Draw vertical separators and the 'x'
            line = ""
            for col in range(1, n * 2 + 2):
                if col % 2 == 1:
                    line += "| "
                elif row // 2 == y and col // 2 == x:
                    line += "x "
                else:
                    line += "  "
            print(line.rstrip())  # Ensure no trailing spaces

# Get user input
n = int(input("n: "))
x = int(input("x: "))
y = int(input("y: "))

# Draw the grid
draw_grid(n, x, y)