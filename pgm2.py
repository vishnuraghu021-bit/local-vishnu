try:
    a=int(input("enter first number:"))
    b=int(input("enter the second number:"))
    print(f"before swapping:a = {a},b = {b}")
    a,b=b,a
    print(f"after swapping:a = {a},b = {b}")
except ValueError:
    print("please enter valid integers.")