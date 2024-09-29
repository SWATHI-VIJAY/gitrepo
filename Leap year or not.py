def is_leap_year(year):
    return ((year%4==0 and year%100!=0) or (year%400==0))
years=int(input("enter a number:"))
check=is_leap_year(years)
print(f"the given year{years} is a leap year:{check}")