# keyword arguments --- an argument preceded by an identifier helps with readability order of arguments doesn't matter
#                           positional, default, keyword, arbitrary

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=654, first=8697, last=1235)

print(phone_num)