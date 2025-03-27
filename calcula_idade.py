from datetime import datetime

dateOfBirth = input("Type your date of birth: ")
born = datetime.strptime(dateOfBirth, "%d/%m/%y")
today = datetime.today()
age = today.year - dateOfBirth

print(f"You are {age} years old.")