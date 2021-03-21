import datetime

current_time = datetime.datetime.now()
print("Date and Time  : ", end="")
print(current_time)

print("Year : ", end="")
print(current_time.year)

print("Month : ", end="")
print(current_time.month)

print("Day : ", end="")
print(current_time.day)

print("Hour : ", end="")
print(current_time.hour)

print("Minute : ", end="")
print(current_time.minute)

print("Second : ", end="")
print(current_time.second)

print("Microsecond : ", end="")
print(current_time.microsecond)

today = datetime.date.today()

d1 = today.strftime("%m/%d/%Y")
print("date in US style =", d1)

d2 = today.strftime("%B %d, %Y")
print("text style =", d2)
