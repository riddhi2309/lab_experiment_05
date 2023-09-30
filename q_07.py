# Getting input by the user
n =int(input("Enter the number:-"))
m =(2*n) - 2
#Starting the if condtion
for i in range (0 ,n):
    #staring the nested if condition
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print("*", end =' ')
    print()



