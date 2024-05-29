# mystring = "helloworld"
# print("hello" in mystring ) #True
# print("abcd" in mystring) #False
#
# print('hello' not in mystring ) #False
# print('abcd' not in mystring ) #True

# iterating string using for loop

# mystring = "Welcome"
#
# for i in mystring:
#     print(i, end = "abc")
#
# print("abcd123".isalnum())  # True
# print("@#$%^".isalnum())  # False
# print("abcd".isalpha())  # True
# print("abcd123".isalpha())  # False
# print("abcde".islower())  # True
# print("AbcdeF".islower())  # False
# print("BSCSS".isupper())  # True
# print("ASNcc".isupper())  # False
# print("666123".isdigit())  # True
# print("abcd12".isdigit())  # False
# print(" ".isspace())  # True
# print(" e  ".isspace())  # False
# print("Hello, Its Python".istitle())  # True
# print("This is Not title".istitle())  # False

# mytxt = "Hello,welcome to my world, welcome to python"
#
# print(mytxt.find("welcome")) # 6
# print(mytxt.find("magic")) # -1
# print(mytxt.rfind("welcome")) # 27
# print(mytxt.rfind("magic")) # -1
# print(mytxt.replace("welcome", "banana"))
# print(mytxt.count("welcome")) #2


mytxt = "Hello,Welcome to my world, welcome to Python"

print(mytxt.startswith("Hello")) # True
print(mytxt.startswith("welcome")) # False
print(mytxt.endswith("Python")) # True
print(mytxt.endswith("world")) # False
print(mytxt.lower()) # hello,welcome to my world, welcome to python
print(mytxt.upper()) # HELLO,WELCOME TO MY WORLD, WELCOME TO PYTHON
print(mytxt.capitalize()) #Hello,welcome to my world, welcome to python
print(mytxt.title()) #Hello,Welcome To My World, Welcome To Python
print(mytxt)





