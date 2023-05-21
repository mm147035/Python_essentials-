# map

# def multiply_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(list(map(multiply_2,[1,2,3])))

my_list =[1, 2, 3]
def multiply_2(item):
    return item*2


print(list(map(multiply_2,my_list)))