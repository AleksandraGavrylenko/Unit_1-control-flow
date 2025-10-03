#syntax
'''
initialize variable
while condition:
    code block
    use variable (+ / -)
'''
num = 5
while num >=1:
    print(num)
    num -=1
print('blast off') 

sum = 0
num = 0
# while num <=10:
#     sum += num 
#     num += 1
# print(sum) 
while num <=10:
    sum+=num 
    if num < 10:
        print(num, end=' + ')
    else:
        print(num, end=' = ')
    num +=1
print(sum)
# sum of digits: take user input as int, and find the sum of it's digits. 
# number = '1234' #input('enter a number')
# sum = 0
# for char in number:
    #print(f'{char} {type(char)}')
    # sum += int(char)
# print(sum)

# i=0
# while i<len(number):
#     sum+= int(number[i])
#     i +=1
    

#algorithm for sum digits
n = 1234 #int(input('enter a number'))
number = n 
sum = 0
while number > 0:
    digit = number % 10 #get the last digit
    sum += digit # add to sum
    number = number // 10 #remove last digit

print(f'sum of digits of {n}: {sum}')

#algorithm for count digits
number = 543215 
count = 0
while number > 0:
    count +=1
    number = number // 10
    
print(count)