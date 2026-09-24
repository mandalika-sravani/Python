# Match-case statement (switch) --- An alternative to using many 'elif' statements. Execute some code if a value matches 
#                                       a 'case'-- by these code is cleaner and syntax is readable

def day_of_week(day):
    match day:
        case 1:
            return "It is a Sunday"
        case 2:
            return "It is a Monday"
        case 3:
            return "It is a Tuesday"
        case 4:
            return "It is a Wednesday"
        case 5:
            return "It is a Thursday"
        case 6:
            return "It is a Friday"
        case 7:
            return "It is a Saturday"
        case _:
            return "Not a valid day"

print(day_of_week("ssbj"))