a=int(input("Enter First Num:"))
b=int(input("Enter Second Num:"))
num=int(input("1) Addition \n2) Substraction \n3) Multiplication \n4) Division"))
if num == 1:
    print("Addition =",(a+b))
elif num == 2:
    print("Substraction =",(a-b))
elif num == 3:
    print("Multiplication =",(a*b))
elif num == 4:
    print("Division =",(a/b))
else:
    print("Invalid Choice")