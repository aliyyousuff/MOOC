__author__ = 'aliyyousuf@gmail.com'



NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)

# print the matrix
trace = 0
for rc in range(0,NUM_COLS):
     #print(my_matrix[rc][rc])
     trace += my_matrix[rc][rc]
print(trace)
