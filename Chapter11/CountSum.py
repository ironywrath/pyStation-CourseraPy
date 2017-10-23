import re

files_lst = ['regex_sum_42.txt','regex_sum_35392.txt']
file_name = None

while True:
    file_No = input("Please enter 1 or 2 to select file: ")
    if file_No == str(1):
        file_name = files_lst[0]
        break
    elif file_No == str(2):
        file_name = files_lst[1]
        break
handle = open(file_name)
number_lst = list()
for line in handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    if len(numbers) > 0:
        for num in numbers:
            number_lst.append(int(num))

print(sum(number_lst))


