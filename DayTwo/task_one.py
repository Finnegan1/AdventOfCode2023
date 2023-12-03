import re

sum = 0

available = {
        "red": 12,
        "green":13,
        "blue":14,
}

with open('input.txt', 'r') as f:
    for game_number, line in enumerate(f, 1):
        possible = True
        for played_set in line.split(":")[1].split(";"):
            for color in available.keys():
                pattern = "\d*(?= "+ color +")"
                result = re.search(pattern, played_set)
                if result == None:
                    continue
                if int(result.group(0)) > available[color]:
                    possible = False
                    break
            if not possible:
                break 
        if possible:
            sum = sum + game_number
print(sum)
