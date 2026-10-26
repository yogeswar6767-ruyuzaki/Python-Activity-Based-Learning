# program to find Calendar Generator

days_in_month = int(input("How many days are in the month? "))

print("Sun Mon Tue Wed Thu Fri Sat")

day = 1

while day <= days_in_month:
    for i in range(7):
        if day <= days_in_month:
            print(day, end="  ")
            day = day + 1
    print()