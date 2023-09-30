#getting the input by the user 
N = int(input("Enter the number :-"))
# Intialize by the i = 1
i = 1
# starting the while loop 
while i<=N:
# intializig another variable
    f = 1
    # using nested loop
    while f<=20:
       print(i,"x", f ,"=", i*f)
       f+=1
    i+=1
