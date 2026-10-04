is_holiday = input ("IS today a holiday? (yes/no): ")
if is_holiday.lower() == "yes":
    print("Yay! Enjoy your holiday!")
elif is_holiday.lower() == "no":
    print("Oh! It's a working day.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")