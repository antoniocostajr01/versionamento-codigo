from datetime import datetime

dateOfBirth = input("Type your date of birth: ")
born = datetime.strptime(dateOfBirth, "%d/%m/%Y")
today = datetime.today()
age = today.year - born.year

print(f"You are {age} years old.")