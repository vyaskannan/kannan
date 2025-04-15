#Compare the length of your first name and your last name
first_name = "vyas"
last_name = "sn"
length_of_first_name = len(first_name)
length_of_last_name = len(last_name)
print("Length of first name:", length_of_first_name)
print("Length of last name:", length_of_last_name)
if length_of_first_name > length_of_last_name:
    print("First name is longer than last name")
elif length_of_first_name < length_of_last_name:
    print("Last name is longer than first name")
else:
    print("First name and last name are of equal length")
#Use the string formatting method to display your full name
