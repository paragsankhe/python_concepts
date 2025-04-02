# numbers = [1,2,3,4,5]
#
# #output [1,4,9,16,25]
#
# #define function to sqr number
# def square(number):
#     return number ** 2
#
# #map object that will perform and find square of each number in list
# square_result = map(square,numbers)
#
# #convert map object to list
# print(list(square_result))

#using lambda funcn within map()
# numbers = [1,2,3,4,5]
# #output [1,4,9,16,25]
# square_result = map(lambda x : x ** 2,numbers)
# #converting map object to list
# print(list(square_result))

#multiple iterables inside map()
number_list1 = [1,2,3,4]
number_list2 = [5,6,7,8]

def add(x,y):
    return x + y

add_result = map(add,number_list1,number_list2)

result_add_list = list(add_result)

print(result_add_list)
















