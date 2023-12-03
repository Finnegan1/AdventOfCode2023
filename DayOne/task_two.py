def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

sum = 0
with open('input.txt', 'r') as f:
    for line_index, line in enumerate(f, 0):
        found = {}
        for number, number_text in enumerate(numbers, 0):
            number = number % 9 + 1
            f_index_list = find_all(line, number_text)
            for f_index in f_index_list:
                found[f_index] = number
        min_key = min(found.keys())
        max_key = max(found.keys())
        sum = sum + int(str(found[min_key]) + str(found[max_key]))
print(sum)
