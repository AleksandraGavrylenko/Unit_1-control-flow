#while ... else
'''
The else clasue runs when:
the loop completes normaly w/out hitting a break
'''
#basic ex 1
count = 1 
while count <= 3:
    print(count)
    count += 1
else:
    print('loop completed')
    
#basic ex 2
count = 1 
while count <= 5:
    print(count)
    if count == 3:
        break
    count += 1
else:
    print('this wont print')
    
