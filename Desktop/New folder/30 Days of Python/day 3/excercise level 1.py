#1 Declare your age as integer variable
age = int(input("Enter your age: "))
print("Your age is:", age)  
#2 Declare your height as a float variable
height = float(input("Enter your height in meters: "))
print("Your height is:", height)
#3 Declare a variable that store a complex number
number = complex(input("enter the number"))
print("number =", number)
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
height = int(input("Enter Height"))
Base = int(input("Enter Base"))
area_of_the_triangle = 0.5 * Base * height
print("area_of_the_triangle =", area_of_the_triangle)
#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a ="))
b = int(input("Enter side b ="))
c = int(int(input("Enter side c =")))
perimeter_of_triangle = a + b + c
print([perimeter_of_triangle])
#6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("enter length"))
width = int(input("Enter width"))
area_of_rectangle = length * width
perimeter = 2 * (length + width)
print("area", area_of_rectangle)
print("perimeter",perimeter)
#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Enter the r ="))
pi = 3.14
area = pi * r * r
print("area pf the circle", area)
c = 2 * pi * r
print("circumference of circle", c)
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Equation: y = 2x - 2

# Coefficients
slope= 2           # Slope
b = -2          # Y-intercept

# Calculate x-intercept by setting y = 0
# 0 = 2x - 2 => x = 1
x_intercept = (0 - b) / slope

# Display results
print("Slope (slope):", slope)
print("Y-intercept (b):", b)
print("X-intercept:", x_intercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m = (y2 - y1) / (x2 - x1)
print("m:", m)
#Compare the slopes in tasks 8 and 9.
if m == slope:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")
#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = int(input("Enter the value of x: "))
y = x**2 + 6*x + 9
print("The value of y is:", y)
# The value of y will be 0 when x = -3 (the roots of the equation)
#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len("python")
len_dragon = len("dragon")
if len_python == len_dragon:
    print("The lengths are equal.")
else:
    print("The lengths are not equal.")
#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in "python" and 'on' in "dragon":
    print("The substring 'on' is found in both words.")
else:
    print("The substring 'on' is not found in both words.")
#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if 'jargon' in "I hope this course is not full of jargon":
    print("The word 'jargon' is found in the sentence.")
else:
    print("The word 'jargon' is not found in the sentence.")
#15 There is no 'on' in both dragon and python  
# Use in operator to check if 'on' is not found in both dragon and python
if 'on' not in "dragon" and 'on' not in "python":
    print("The substring 'on' is not found in both words.")
else:
    print("The substring 'on' is found in at least one of the words.")
#Find the length of the text python and convert the value to float and convert it to string
len_python = len("python")
float_len_python = float(len_python)
str_len_python = str(float_len_python)
print("Length of 'python' as string:", str_len_python)
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# 0 is even, 1 is odd, 2 is even, 3 is odd, 4 is even, 5 is odd, 6 is even, 7 is odd, 8 is even, 9 is odd
# 10 is even, 11 is odd, 12 is even, 13 is odd, 14 is even, 15 is odd, 16 is even, 17 is odd, 18 is even, 19 is odd 
# 20 is even, 21 is odd, 22 is even, 23 is odd, 24 is even, 25 is odd, 26 is even, 27 is odd, 28 is even, 29 is odd
# 30 is even, 31 is odd, 32 is even, 33 is odd, 34 is even, 35 is odd, 36 is even, 37 is odd, 38 is even, 39 is odd
x = int(input("Enter a number: "))
if x % 2 == 0:
    print(x, "is even.")
else:
    print(x, "is odd.")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_value = int(2.7)
if floor_division == int_value:
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7.")
else:
    print("the floor division is no equal ")
#19 Check if type of '10' is equal to type of 10
a = '10'
b = 10
if str(b) == a:
    print("The values are equal when converted to the same type.")
else:
    print("The values are not equal.")
#Check if int('9.8') is equal to 10
if int(float('9.8')) == 10:
    print("int('9.8') is equal to 10.")
else:
    print("int('9.8') is not equal to 10.")
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours worked: "))
rate_per_hour = int(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Total pay:", pay)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred year
years = int(input("Enter number of years you have lived: "))
seconds_in_a_year = 365 * 24 * 60 * 60
seconds_lived = years * seconds_in_a_year
print("You have lived approximately", seconds_lived, "seconds.")
#Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
#Write a script that prompts the user to enter a number of days. Calculate the number of seconds in a day.