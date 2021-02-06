print("Enter the year to check if it's a leap year\n")
year = int(input())

print(f"Checking if {year} is a leap year")

if year % 4 != 0:
    print(f"Year {year} is not a leap year")
else:
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 400 != 0):
        print(f"Year {year} is a leap year")
    else:
        print(f"Year {year} is not a leap year")
