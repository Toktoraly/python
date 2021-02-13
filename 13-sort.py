numbers = [65,2,6,3,7,2,7,8,5,2]
num_len = len(numbers)
for i in range(num_len):
    current_num = numbers[i]
    for e in range(num_len):
        if numbers[e]< current_num:
            numbers[i],numbers[e] = numbers[e],numbers[i]
print(numbers)