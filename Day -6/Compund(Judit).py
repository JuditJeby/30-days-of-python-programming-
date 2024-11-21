principle_amount=int(input("Enter the principle amount"))
rate_of_interest=int(input("Entrr the rate of interest"))
time_in_years=int(input("Enter the time"))
amount=principle_amount*(1+(rate_of_interest/100))**time_in_years
compound=principle_amount-amount
print(compound)