# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using if-elif-else statements.

def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False
    
year = int(input("Enter a year to determine if it is a leap year: "))
if isleapyear(year):
  print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")