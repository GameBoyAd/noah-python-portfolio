# Leap Year Checker
# Noah Dong


#Init


#Function
def leap_year(year):
    if year % 400 == 0:
        print ("true")
    elif year % 100 == 0:
        print ("false")
    elif year % 4 == 0:
        print ("true")


#Main
leap_year(2024)#True
