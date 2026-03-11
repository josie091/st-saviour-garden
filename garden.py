

if __name__ == '__main__':

    # print without a line break using this function
    # print('🌷', end='')

    print('solid')
    for i in range(11):
        for j in range(11): 
            print('🌷', end= '')
        print('')

    print('horizontal')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0:
                print('🌷', end='')
            else:
                print('🌱', end='')
        print('')

    print('vertical')
    for i in range (11):
        for j in range (11):
            if j % 2 ==0:
                print ('🌷', end='')
            else:
                print('🌱', end='')
        print ('')

    print ('plaid')
    for row in range(11):
        for col in range(11):
            if row % 2 == 0 and col % 2 == 0:
                print ('🌷', end= "")
            else:
                print("🌱", end="")
        print('')

    print('diagonal')
    for row in range (11):
        for col in range(11):
            if row %2 == 0 and col % 2 == 0:
                print ('🌷', end= "")
            elif row %2 ==1 and col% 2 ==1:
                print ('🌷', end= "")
            else:
                print("🌱", end="")
        print('')

    print('cross')
    for row in range(11):
        for col in range(11):
            if row == col or row + col ==10:
                print ('🌷', end= "")
            else:
                print("🌱", end="")
        print ()





        