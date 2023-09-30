#getting the input bythe user 
n = int(input("Enter the number:-"))
#intializing the loop with the variable count , not_count
count = 0
not_count = 0
#getting another input by the user
num = int(input("Enter the number:-"))
#starting the while loop
while num != -999:
    # starting the nested if loop
    if num%n == 0:
        count =count+1
    else:
        not_count= not_count+1
    num  = int(input("Enter a number:-"))
print(count)
print(not_count)    
