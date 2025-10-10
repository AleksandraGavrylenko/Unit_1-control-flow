#pyramid pattern
rows = 5
n = 1
#step 1 create outer loop for rows
for i in range(rows):
    #step 2 print the spaces rows - i -1
    for j in range(rows-i-1):
        print(' ', end='')
    #print the stars 2*i + 1
    for k in range(2*i+1):
        print('*', end='')
    #step 4 print new line 
    print()