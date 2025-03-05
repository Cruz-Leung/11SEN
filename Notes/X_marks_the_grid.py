n = int(input("n: "))
x = int(input("x: "))
y = int(input("y: "))
def draw_grid(n, x, y):
    for row in range(n * 2 + 1):
        if row % 2 == 0:
            print("+ " + "- + " * (n-1) + "- +")
        else:
            line = ""
            for col in range(n):
                if row // 2 + 1 == y and col + 1 == x:
                    line += ("| x ")
                else:  
                    line += ("|   ")
            print(line + "|")
            

draw_grid(n, x, y)
 
# Draws a grid and indentifies the X depending on the coordinate