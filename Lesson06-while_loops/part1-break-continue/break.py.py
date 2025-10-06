#break statement in loops
# break means exit the loop immediately
# use cases
'''
*stop when u find something
*exit early based on condition
*get out of infinite loops
'''
count =  1
while count <= 10:
    print(count)
    if count == 5:
        break
    count += 1

while True:
    choice = input('enter smth (q for quit)')
    print(f'you entered {choice}')
    if choice == 'q':
        print('u want to exit')
        break
    print(f'u entered {choice}')
    
#algorithm find first divisor
n = 15
divisor = 2
while True:
    if n % divisor == 0:
        print('found it')
        print(divisor)
        break