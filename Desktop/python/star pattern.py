rows = int (input('enter the rows : ='))
for i in range( 1, rows +1):
        for j in range (0,i):
            print('*',end ='')
            print()
        for i in range( 1 , rows):
            for j in range (rows -i , 0, -i):
                print('*',end ='')
            print()    