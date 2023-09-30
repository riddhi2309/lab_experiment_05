#getting the input by the user 'N'
N = int(input("Enter the number"))
#initializing by i = 1
i =0
#starting the while loop
while i<N:
#creating the new variable f    
    f =N
#Nested while loop where f is >= 0
    while f>=0:
       b = (2*i) - 1
       print(' '*f,'*'*b)
       f-=1
       i+=1