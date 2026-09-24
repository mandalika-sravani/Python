# *args --- allows you to pass multiple non-key arguments
# **kwargs --- allows you to pass multiple key arguments

# *args

def display_name(*names):
    for name in names:
        print(name, end=" ")

#display_name("Manav", "Naresh", "Rohit", "Charan", "Ram", "Vamsi", "Chaitra", "Krishna", "Aman")

# **kwargs

def address(**address):
    for key, value in address.items():
        print(f"{key} : {value}")

#address(street = "Sri Lakshmi Nagar",
#        apt= "Bhoomi Enclave",
#        city ="Hyderabad",
#        state = "Telangana",
#        pin = "500036")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Manav", "Naresh", "Rohit", "Charan",
               street = "Sri Lakshmi Nagar",
                apt= "Bhoomi Enclave",
                city ="Hyderabad",
                state = "Telangana",
                pin = "500036")