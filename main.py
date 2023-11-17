my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

if len(my_list) > 1:
    result_list = [my_list[-1]] + my_list[:-1]
else:
    result_list = my_list

print(result_list)
