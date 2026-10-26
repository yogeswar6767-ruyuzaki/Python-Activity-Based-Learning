# program to find Attendance Recovery

classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
required_percentage = float(input("Enter the required attendance percentage: "))

new_classes = 0

while (classes_attended / classes_held) * 100 < required_percentage:
    classes_held = classes_held + 1
    classes_attended = classes_attended + 1
    new_classes = new_classes + 1

print("More classes to attend:", new_classes)