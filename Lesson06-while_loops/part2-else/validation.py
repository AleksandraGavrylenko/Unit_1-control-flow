# input validation 1 > username validation
while True: 
    username = input('enter username (3-15 chars)')
    if len(username) < 3:
        print('too short min 3 chars')
        continue
        
    if len(username) > 15:
        print('too long, max 15 chars')
        continue 
    #check if username has any spaces
    has_space = False 
    for char in username:
        if char == " ":
            has_space = True
            break 

    if has_space:
        print('no spaces allowed')
        continue
    # username validation passed
    print(f'Username "{username}" accepted!\n')
    break
