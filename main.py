#Ask what the max mark is and recieve the input
print("What is the Maximum mark you can get?")
maxmark = int(input())

#Same thing as above but for the mark they recived
print("What mark did you recieve?:")
markrecieved = int(input())

#Print percentage
calculatedgrade = markrecieved / maxmark * 100

#Calculate Grade
if 90 <= calculatedgrade <= 100:
    grade = "A+"
elif 80 <= calculatedgrade <= 89:
    grade = "A"
elif 75 <= calculatedgrade <= 79:
    grade = "B+"
elif 70 <= calculatedgrade <= 74:
    grade = "B"
elif 65 <= calculatedgrade <= 69:
    grade = "C+"
elif 60 <= calculatedgrade <= 64:
    grade = "C"
elif 55 <= calculatedgrade <= 59:
    grade = "D+"
elif 50 <= calculatedgrade <= 54:
    grade = "D"
elif 45 <= calculatedgrade <= 49:
    grade = "E+"
elif 40 <= calculatedgrade <= 44:
    grade = "E"
else:
    grade = "UG"

rounded = round(calculatedgrade,2)
print("Your percentage:")
print(rounded,"%")
print("Your grade:")
print(grade)