text = input('enter a text')
#initizlize counters
total_chars = len(text)
letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0

#track first and last char
first_char = None 
last_char = None 

print(f'Analyzing: "{text}"')
print('='*40)

#proccess each char
for char in text:
    if 'A' <= char <='Z' or 'a'<=char<='z':
        letter_count +=1
        if first_char == None:
            first_char = char
        last_letter = char 
    if 'A' <=char<='Z':
        uppercase_count +=1
    if 'a' <=char<='z':
        lowercase_count +=1
    if '0' <=char<='9':
        digit_count +=1
        
#display results 
print(f'Total chars: {total_chars}')
print(f'Total letters: {letter_count}')
print(f'Total lowercase: {lowercase_count}')