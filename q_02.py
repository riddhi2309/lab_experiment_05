#get the input by the user 'N'
N = int(input("enter the number:- "))
#Intializing the while loop with i=1
i = 1
#starting the while loop with i<=1000
while i<= 1000:
#condition the if loop
    if i%N != 0:
        print(i)
    i+=1
