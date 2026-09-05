principle_amount=int(input("Enter the principle amount: "))
interest=int(input("Enter the rate of interest: "))
interest/=100
time=int(input("Enter the time in years: "))
print("does the compound interest is calculated for every month or for every year\n if for every year enter 1 or for every month enter 2.")
a=int(input("please enter 1 or 2: "))
total_amount=0
if a==1:
    total_amount=principle_amount*((1+(interest))**(time))
elif a==2:
    total_amount=principle_amount*((1+(interest/12))**(12*time))
else:
    print("enter valid details")
print("The total amount you can get :",total_amount)
print(f"The total profit earned in {time} years :",total_amount-principle_amount)

