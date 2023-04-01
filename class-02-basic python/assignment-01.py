# Assignment

# 1 Print your name.
name = input("write your name")
print("My name is " + name)
# 2 Input your batch number using input() function.

batch = input('input your batch number')
print("My batch number is" + batch)

# 3 Create 5 different valid Variables and print.
# type-01
_power = 2
print("variable name is _power", _power)
# type-02
power = 3
print("variable name is power", power)
# type-03
power01 = 4
print("variable name is power01", power01)
# type-04
ints = 5
print("variable name is lists", ints)

# type-05-Snake Case
power_number = 6
print("variable name with Snake Case format is power_number", power_number)

# 4 Create Pascal Case Variable.
PowerNumber = 10
print("variable name with Pascal Case format is PowerNumber", PowerNumber)

# 5 Assign a single value to Multiple variables with memory location.
x = y = z = 10
print("value of x, y, z are respectively", x, y, z)
print("Memory Allocation of x is", id(x))
print("Memory Allocation of y is", id(y))
print("Memory Allocation of z is", id(z))

# 6 Input float value using input().
number = float(input('write a float number'))
print("value of float is", number)
print("type: ", type(number))

# 7 a = ‘Welcome to Django for web and Ai’ convert into upper case.
a = "Welcome to Django for web and Ai"
print("upper case of that sentence: ", a.upper())

# 8 b = ‘    Python’ remove whitespace.
# note: we use strip to remove whitespace before start of a sentence
b = "              Python"
print("remove whitespace using b.strip():", b.strip())

# 9 c = 60, d= 22 ‘Conversion int to float’.
c = 60
d = 22
print("type of c:", type(c))
print("type of d:", type(d))

c = float(c)
d = float(d)

print("after conversion, type of c is {} and value is {}".format(type(c), c))
print("after conversion, type of d is {} and value is {}".format(type(d), d))

# 10 Create a dictionary & print your info.

my_dict = {"last_name" : "Nomani",
           "first_name" : "Shibli",
           "employment_status" : "employed",
           "nationality" : "Bangladeshi",
           "city" : "Dhaka"}
print("This is my info dictionary:","\n", my_dict)
