TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator \n")

# cent_per_kWh = int(input("Enter cents per kWh: "))
tariff_choice = int(input("Which tariff? 11 or 31: "))
while tariff_choice != 11 and tariff_choice != 31:
    print("invalid choice. try again")
    tariff_choice = int(input("which tariff? 11 or 31: "))

daily_use_kWh = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))

if tariff_choice == 11:
    cost_per_day_in_dollars = TARIFF_11 * daily_use_kWh
else:
    cost_per_day_in_dollars = TARIFF_31 * daily_use_kWh

estimated_bill = number_of_days * cost_per_day_in_dollars
print("estimated bill: $ {:.2f}".format(estimated_bill))
