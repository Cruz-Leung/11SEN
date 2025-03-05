import array

matrix = [ 
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), # the i indicates it is an integer
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), 
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), 
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), 
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), 
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), 
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), 
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), 
    array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9]), 

]

# print(matrix[1][1])
# matrix[1][1] = "Five"
# true arrays can only accept 1 data type

# for loop 
for row in matrix:
    for col in row:
        print(col)
        print(row)
        



# while loop