with open('numbers.txt', 'r') as file:
    number = file.readlines()

squared_numbers = [str(int(num.strip()) ** 2) + "\n" for num in number]

with open('results.txt', 'w') as doc:
    doc.writelines(squared_numbers)

print(squared_numbers)
