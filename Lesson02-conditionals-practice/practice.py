age_input = input('enetr ur age')
rating = input('enter movie rating: R, G, PG, or PG-13 in that exact format')
if age_input and rating:
    age = int(age_input)
    if rating == 'R':
        if age >= 17:
            print('movie rated R, u can watch')
        else:
            print('movie rated R too young. dont watch')
    elif rating == 'PG-13':
        if age >= 13:
            print('u can watch, movie rating PG-13')
        else:
            print('u can watch, adult guidance recomended, movie rating PG_13')
    elif rating == "PG":
        if age >= 6:
            print('movie rated PG. u can watch.')
        else:
            print('movie rated PG. ur too young')
    elif rating == 'G':
        if age >= 0:
            print('movie rated G. u can watch')
    else:
        if age < 0:
            print('enetr valid age')
        elif rating != ('R' or 'PG-13' or 'PG' or 'G'):
            print('invalid rating input.')
        else:
            print('error')
else:
    print('enter a valid number for age')