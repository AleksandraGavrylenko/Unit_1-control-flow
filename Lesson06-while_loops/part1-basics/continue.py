#continue statement
'''
skips to the next iteration
break - completely exits
continue - skips current iteration
'''

count = 0
while count < 5:
    count +=1
    if count == 3:
        continue 
    print(count)
