print("-------------------------List Functions----------------\n")
#############################################################
friends = ["fab", "tuyg", "james", "jane", "jane", "jane","claire", "muhire", "simoni"]
number = [2, 9, 4, 3, 5, 31, 42, 51, 13]

# friends.extend(number)          # Add lists (friends and number)
# friends.append("Moise")         # Add item to a list
friends.insert(4, "Deborah")    # Insert item on index[4]
# friends.remove("claire")
# friends.pop()
friends.sort()
number.reverse()
number.sort()


friends2= friends.copy()

print(friends.index("simoni"))
print(friends.count("jane"))
print(friends)
print(number)

print(friends2)
##############################################################
print("\n---------------------------Python----------------------")
