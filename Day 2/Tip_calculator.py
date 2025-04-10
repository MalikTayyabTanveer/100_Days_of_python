print("welcoome to the tip calculator")

total_bill = float(input("what is your total bill? $\n"))
tip = int(input("how much would like to give tip? 10, 12 or 15? "))

total_bill += total_bill * (tip / 100)
print(total_bill) 

person = int(input("how many people to split the bill? "))

total_bill = round(total_bill / person,2)

print(f"each person should pay: ${total_bill}")