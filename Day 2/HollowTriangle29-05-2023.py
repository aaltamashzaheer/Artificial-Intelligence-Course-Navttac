row = int(input('Enter number of rows you require to create a Hollow Triangle: '))

for i in range(1,row+1):
    for j in range(1,2*row):
        if i==row or i+j==row+1 or j-i==row-1:
            print('*',end='')
        else:
            print(' ', end='')

   
    print() # printing new line