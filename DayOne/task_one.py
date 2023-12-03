sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        first_number = ""
        second_number = ""
        for element in line:
            print(element)
            if element.isnumeric() :
                if first_number == "":
                    first_number = element
                    second_number = element
                else:
                    second_number = element
        sum = sum + int(first_number + second_number)
print(sum)
