#reverse number 
rows = int (input('enter the rows: ='))
for i in range ( rows):
    for j in range (rows -i ,0, -1):
     print (j , end =' ')
     print() 