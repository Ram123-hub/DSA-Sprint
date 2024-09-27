def leap_year(year):
    if (year % 4 == 0 or year % 400 == 0):
        print("Year is a leap year")
    else:
        print("Year is not a leap year")


num = int(input("Enter an year:  "))
leap_year(num)
