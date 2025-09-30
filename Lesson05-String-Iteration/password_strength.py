strong_password = False
length_good = False 
Up_good = False
Low_good = False 
digit_good = False
special_good = False
count_up = 0
count_lw = 0
count_dg = 0
count_sp = 0
char_row = ''
char_num = 0
repetition = False
bad_seq_val = ['abc','123']
bad_seq = False
points = 10


password = input('enter password')
if len(password) >=8:
    length_good = True
for char in password:
    if 'A' <= char <= 'Z':
        Up_good = True
        count_up += 1
    elif 'a' <= char <= 'z':
        Low_good = True
        count_lw += 1
    elif '0' <= char <= '9':
        digit_good = True
        count_dg += 1
    elif char != ' ':
        special_good = True
        count_sp += 1

    if char_row == char:
        char_num += 1
        if char_num >= 3:
            repetition = True
    else:
        char_row = char 
        char_num = 0

if length_good and Up_good and Low_good and digit_good and special_good:
    strong_password = True
        
for i in bad_seq_val:
    if i in password:
        bad_seq = True
        
if repetition:
    points -= 2
if bad_seq:
    points -=2
    
print('password analysis')
print(f'password: {password}')
print(f'char count')
print(f'length: {len(password)}')
print(f'#upper: {count_up}')
print(f'#lower: {count_lw}')
print(f'#digit: {count_dg}')
print(f'#special: {count_sp}')
print(f'requirements check')
print(f'length: {length_good}')
print(f'length: {Up_good}')
print(f'length: {Low_good}')
print(f'length: {digit_good}')
print(f'length: {special_good}')
print('issues')
print(f'repeated chars: {repetition}')
print(f'bad seq: {bad_seq}')
if points == 10:
    print('strong')
elif points == 8:
    print('medium')
else:
    print('weak')