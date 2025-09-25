#three forms of range function
#1 range(stop)
for i in range(5):  #0,1,2,3,4
    print(i)
#2 range(start,stop)   #3,4,5,6,7
for i in range(3,8):
    print(i)
#3 range(start,stop,step)   #2,4,6,8,10
for i in range(2,11,2):
    print(i)
# counting backwards
for i in range(10,1,-2):  #10,8,6,4,2
    print(i)
    
print('=====================')
# ex 1
#countdown timer from 10-0
import time
for i in range(10,-1,-1):
    print(f'seconds - {i}')
    time.sleep(0.2) #wait 0.2 sec between numbrs
    if i == 0:
        print(f'🚀🚀🚀🚀 BLAST OFF! 🚀🚀🚀🚀')
        
#multiplication table
#take user input for the num and print table number * 1 = number etc
number_input = int(input('enter a number (1-12): '))
if 1<=number_input<=12:
    number = number_input
    for i in range(1,13):
        result = number * i
        print(f'{number} x {i:2d} = {result:3d}')
else:
    print('enter a num between 1 and 12')