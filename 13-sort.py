numbers = [65,2,6,3,7,2,7,8,5,2]
num_len = len(numbers)
for i in range(num_len):
    for e in range(num_len):
        if numbers[i]< numbers[e]:
            numbers[i],numbers[e] = numbers[e],numbers[i]
print(numbers)