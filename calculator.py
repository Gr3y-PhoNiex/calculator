name = raw_input("Please Enter Your Name:")
print("Welcome To My Calculator",name)
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
x = a+b
y = a-b
z = a*b
v = a/b
print("What You Want To Do?")
print("1.Plus")
print("2.Minus")
print("3.Multiply")
print("4.Division")
answer = int(input("Please Enter Only Number:"))
if answer == 1:
    print("{} + {} = {}".format(a , b , x))
elif answer == 2:
    print("{} - {} = {}".format(a , b , y))
elif answer == 3:
    print("{} * {} = {}".format(a , b , z))
elif answer == 4:
    print("{} / {} = {}".format(a , b , v))
