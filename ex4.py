first_list = ['a', 'b', 'c']
update_list = ['a', 'd', 'e']
result_list = []

result_list = list(set(first_list) ^ set(update_list))

result_list.sort()

print(result_list)
