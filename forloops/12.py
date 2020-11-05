
num1=int(input("enter the number you want it to start: "))
num2=int(input("enter the number you want to finnish: "))

for a in range(num1,num2):
    if a > 1:
        for b in range(2,a):
            if (a % b)==0:
                break
        else:
            print(a)