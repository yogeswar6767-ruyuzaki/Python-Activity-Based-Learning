# program to find Nested Loop Seating Generator

rows = int(input("Enter the number of rows: "))
seats_in_each_row = int(input("Enter seats in each row: "))

for row in range(1, rows + 1):
    for seat in range(1, seats_in_each_row + 1):
        print("Row", row, "Seat", seat)