import math

k = 1
d = 5

axis = [i*k for i in range(d+1) if i*k<=d]
total_axis_count = len(axis)*len(axis)
squares = [i ** 2 for i in axis]
over_axis_count = 0


for x in reversed(axis):
    if math.sqrt(x**2 + axis[-1]**2) <= d:
        break
    for y in reversed(axis):
        if math.sqrt(x ** 2 + y ** 2) > d:
            over_axis_count += 1
        elif math.sqrt(x ** 2 + y ** 2) <= d:
            break
        

answer = total_axis_count - over_axis_count

answer = 0
for i in range(0, d + 1, k):
    y = math.sqrt(d ** 2 - i ** 2)
    answer += math.floor(y / k) + 1

print(answer)
