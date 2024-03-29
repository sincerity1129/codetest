n =4
title = "수박"
if n%2 == 0:
    a = title*(n//2)
else:
    n = n-1
    a = title*(n//2) + "수"
    
print(a)