survey = ["AN", "CF", "MJ", "RT", "NA"]
types = ["JM", "RT", "CF", "AN"]
choices = [5, 3, 2, 7, 5]	
score = [3,2,1,0,1,2,3]
from collections import defaultdict
total_type = defaultdict(int)
for type, choice in zip(survey, choices):
    if choice-1 > 3:
        total_type[type[1]] += score[choice-1]
    else:
        total_type[type[0]] += score[choice-1]
        
          
result = ""
for type in types:
    if total_type[type[0]] >=  total_type[type[1]]:
        result += type[0]
    else:
        result += type[1]
          
result = list(result)
index = 0
for alpabet in result:
    if index == 3:
        break
    if total_type[result[index]] < total_type[result[index+1]]:
        result[index] = result[index+1]
        result[index+1] = alpabet
    elif total_type[result[index]] == total_type[result[index+1]]:
        result = sorted(result[index:index+2])
    index += 1
print(result)

"TCMA"