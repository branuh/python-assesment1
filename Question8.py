# Prompt the user to enter a number between 1 and 7
day_number = int(input("Enter a number (1-7): "))

# Determine the corresponding day of the week
if day_number == 1:
    day_name = "Monday"
elif day_number == 2:
    day_name = "Tuesday"
elif day_number == 3:
    day_name = "Wednesday"
elif day_number == 4:
    day_name = "Thursday"
elif day_number == 5:
    day_name = "Friday"
elif day_number == 6:
    day_name = "Saturday"
elif day_number == 7:
    day_name = "Sunday"
else:
    day_name = "Invalid input"
# Print the corresponding day of the week
print("The day is:", day_name)