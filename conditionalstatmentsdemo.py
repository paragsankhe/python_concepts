# nested if else

a = -9

if a > 0:
    print(" a is positive number")
    if a > 20:
        print("a is greater than 20")
    else:
        print("a is less than 20")
elif a == 0:
    print("a is 0")
else:
    print("a is negative number")