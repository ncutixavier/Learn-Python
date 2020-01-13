print("----------------------Dictionaries in Python----------------")
print("____________________________________________________________\n")
######################################################################
monthconversion={
    "jan":"January",
    "feb":"february",
    "mar":"march",
    "apr":"april",
    "may":"may",
    "jun":"june",
    "jul":"july",
    "aug":"august",
    "sep":"september",
    "oct":"october",
    "nov":"november",
    "dec":"december"
}

print(monthconversion["feb"])
print(monthconversion.get("luv","No available key"))
print(monthconversion.pop("dec"))
######################################################################
print("\n---------------------------Python---------------------------")