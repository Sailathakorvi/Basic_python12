print("**********Multiplication table**********")
while(True):
    n = int(input("enter a number:"))
    if(n==0):
        print("thankyou!!")
        break
    else:
        for i in range(1,11):
            ans = n*i
            print(f"{n}*{i}={ans}")
