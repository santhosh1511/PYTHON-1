##num = int(input("enter a number for check armstrong number"))
##sum = 0
##temp = num
##while temp > 0:
##    digit = temp%10
##    sum = sum+digit**3
##    temp//=10
##if num == sum:
##    print(num,"is an Armstrong number")
##else:
##    print(num,"is not Armstrong number")

##num = int(input("enter a number:"))
##n1,n2 = 0,1
##count = 0
##if num <= 0:
##    print("Please enter a positive integer")
##elif num == 1:
##    print("fibonacci sequence upto",num,":")
##    print(n1)
##else:
##    print("Fibonacci sequence:")
##    while count<num:
##        print(n1)
##        nth = n1+n2
##        n1 = n2
##        n2 = nth
##        count += 1



##num = int(input("enter a number:"))
##sum = 0
##temp = num
##while temp > 0:
##    digit = temp%10
##    sum += digit**3
##    temp//= 10
##if num == sum:
##    print(num,"it is a armstorng number")
##else:
##    print(num,"it is not a armstorng number")




num = int(input("enter a number: "))
n1,n2 = 0,1
count = 0
if num<= 0:
    print("enter a positive number")
elif num == 1:
    print("fibonaccci  of num is",num)
    print(n1)
else:
    print("fibonaci series is")
    while count < num:
        print(n1)
        n3 = n1+n2
        n1 = n2
        n2 = n3
        count +=1


















    
