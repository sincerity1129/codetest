s = "2three45sixseven2three45sixseven2three45sixseven2three45sixseven"

str_to_int_mapping = {
'one': '1',
'two': '2',
'three': '3',
'four': '4',
'five': '5',
'six': '6',
'seven': '7',
'eight': '8',
'nine': '9',
}
    
for word, digit in str_to_int_mapping.items():
    s = s.replace(word, digit)
    
print(float(s))