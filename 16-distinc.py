# numbers = [2,1,1,4,9,2,3,6,8,4,2,6,8]
# distinc_num = []
# for i in numbers:
#     if i not in distinc_num:
#         distinc_num.append(i)
# print(distinc_num)

numbers1 = [3,6,9,21,8,11]
numbers2 = [3,9,2,8,10,11]
numbers3 = []
for i in numbers1:
    if i in numbers2:
        numbers3.append(i)
print(numbers3)