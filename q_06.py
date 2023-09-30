#getting the input by the user
n = int(input("Enter the number you want to take gcd of :-"))
#INtitializing the variable count and i
count= 1
i=1
#starting the while loop
while count <=n:
    num = int(input("Enter a digit:- "))
    count+=1
if n <=0:
    print("Invalid input")
else:
    while n:
        num2=num
        num=n
        n=num2%n  
        i += 1

print(f"GCD of given numbers is {num}") 