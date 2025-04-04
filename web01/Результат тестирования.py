import sys
import json

summ = 0
with open('scoring.json') as file:
    data = json.load(file)
    lst = data['scoring']
    for i, line in enumerate(sys.stdin):
        i += 1
        if line.rstrip() == 'ok':
            for d in lst:
                if i in d["required_tests"]:
                    summ += d["points"] // len(d["required_tests"])
                    break
print(summ)


