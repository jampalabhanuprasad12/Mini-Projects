# this is the python code to find the compound interest.
# here we take the input of principle amount from the user. 
principle_amount=int(input("Enter the principle amount  : "))
interest=int(input("Enter the rate of interest  : "))
# from the below line we convert the interest from the percentage to the decimal form.
interest/=100
time=int(input("Enter the time in years     : "))
print("Does the compound interest is calculated for every month or for every year.\nIf for every year enter 1 or for every month enter 2.")
a=int(input("Please enter 1 or 2 : "))
total_amount=0
#this the formula to find the compound interest for 1 year.
if a==1:
    total_amount=principle_amount*((1+(interest))**(time))
# this is the formula to find the compound interest for every month.
elif a==2:
    total_amount=principle_amount*((1+(interest/12))**(12*time))
else:
    print("Enter valid details")
print("==================================*************===================================")
print("The total amount you can get           :",int(total_amount))
print(f"The total profit earned in {time} years     :",int(total_amount-principle_amount))

