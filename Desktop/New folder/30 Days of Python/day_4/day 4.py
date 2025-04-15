#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
line1 = 'Thirty'
line2 = 'Days'
line3 = 'Of'
line4 = 'Python'
full_string = line1 + ' ' + line2 + ' ' + line3 + ' ' + line4
print(full_string)
#2Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
str1 = 'Coding'
str2 = 'For'
str3 = 'All'
full_string2 = str1 + ' ' + str2 + ' ' + str3
print(full_string2)
#3Declare a variable named company and assign it to an initial value "Coding For All".
#4Print the variable company using print().
company = "Coding For All"
print(company)
#5Print the length of the string on variable company.
company_length = len(company)
print("Length of company string:", company_length)
#Change all the characters to uppercase letters using upper() method.
company_upper = company.upper()
print("Company in uppercase:", company_upper)
#7 Change all the characters to lowercase letters using lower() method.
company_lower = company.lower() 
print("Company in lowercase:", company_lower)
# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company_capitalize = company.capitalize()
print("Company capitalized:", company_capitalize)
company_title = company.title()
print("Company title:", company_title)
company_swapcase = company.swapcase()
print("Company swapcase:", company_swapcase)
#9 Cut(slice) out the first word of Coding For All string.
company_first_word = company[0:6]
print("First word of company string:", company_first_word)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
if "Coding" in company:
    print("The word 'Coding' is found in the company string.")
else:
    print("The word 'Coding' is not found in the company string.")
#11 Replace the word coding in the string 'Coding For All' to 'Python'.
company_replaced = company.replace("Coding", "Python")
print("Company string after replacement:", company_replaced)
 