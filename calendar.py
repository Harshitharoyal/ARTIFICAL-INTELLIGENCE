import calendar

# Get the year and month from the user
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Generate the calendar
cal = calendar.monthcalendar(year, month)

# Print the calendar
print("Mo Tu We Th Fr Sa Su")
for row in cal:
    for day in row:
        if day == 0:
            print("   ", end="")
        else:
            print("{:2} ".format(day), end="")
    print()
