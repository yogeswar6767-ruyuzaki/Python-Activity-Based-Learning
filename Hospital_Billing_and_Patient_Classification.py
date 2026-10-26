# program to find Hospital Billing and Patient Classification

consultation = float(input("Enter consultation charge: "))
test_charge = float(input("Enter test charge: "))
treatment_charge = float(input("Enter treatment charge: "))
age = int(input("Enter patient age: "))

total = consultation + test_charge + treatment_charge

if age >= 60:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total bill:", total)
print("Discount:", discount)
print("Final bill:", final_bill)

if final_bill >= 2000:
    print("Patient classification: High bill")
else:
    print("Patient classification: Normal bill")