from datetime import datetime

dataOfBirth = input("Type your date of birth: ")
born = datetime.striptime(dataOfBirth, "%d/%m/%y")
today = datetime.today()
age = today.year - dataOfBirth

print(f"You are {age} years old.")