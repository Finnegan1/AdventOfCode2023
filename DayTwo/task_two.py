import re

sum = 0

with open('input.txt', 'r') as f:
    for game_number, line in enumerate(f, 1):
        minValues = {
                "red": 0,
                "green": 0,
                "blue": 0,
        } 
        for played_set in line.split(":")[1].split(";"):
            for color in minValues.keys():
                pattern = "\d*(?= "+ color +")"
                result = re.search(pattern, played_set)
                if result == None: continue
                minValues[color] = max(minValues[color],int(result.group(0)))
        calc = 1
        for value in minValues.values():
            if value == 0: continue
            calc = calc * int(value)
        sum = sum + calc

print(sum)
