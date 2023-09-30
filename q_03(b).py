#getting the input by the user 'n'
n =int(input("Enter a number:-"))
#initializing by i = 1
i =1
#starting the while loop
while i<=n:
#creating the new variable f
    f=n
#Nested while loop where f is >= 0
    while f>=0:
        print(' '*f,'*'*i)
        f -= 1
        i += 1