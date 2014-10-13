#if else
x = int(input("Enter the int:"))

if x < 0:
    x = 0
    print("It's negative , changes to zero now")
elif x == 0:
    print("It's zero")
elif x == 1:
    print("It's one")
else:
    print("It's > one")
