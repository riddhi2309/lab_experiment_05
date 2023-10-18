#getting the input by the user
n = int(input("count of number input wanted by the user"))
#intializing the variable count and lcm
count = 1
lcm =1
#starting the while loop
while count<=n:
    num = int(input(f"enter a number{count}:-"))
    a, b = lcm, num
    while b:
        a,b=b,a%b
    temp=a 
    lcm = (lcm * num) // temp
    count+= 1

print(f"LCM of given numbers is {lcm}")


# lcm = numbers[0]
# for i in numbers[1:]:
#     x, y = lcm, i
#     while(y):
#         x, y = y, x % y
#     gcd = x
#     lcm = lcm*i//gcd

# print(lcm)