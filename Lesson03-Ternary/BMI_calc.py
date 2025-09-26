print('BMI calc')
entered_height = float(input('enter height (in): '))
entered_weight = float(input('enter weight (lb): '))
height = entered_height if entered_height >= 0 else print('enter proper value')
weight = entered_weight if entered_weight >= 0 else print('enter proper value')
BMI = (weight/(height*height))*703
status = ('Underweight' if BMI < 18.5 else
          "Normal" if 18.5<=BMI<25 else
          "Overweight" if 25<=BMI<30 else
          "Obese" if BMI >= 30 else
          'error')
print('')
print('=====================')
print('BMI Health Report')
print('=====================')
print(f'height: {height}"')
print(f'weight: {weight}')
print(f'BMI: {BMI}')
print(f'category: {status}')
if status == 'Underweight':
    print('Recomendation: Gain Weight')
    print('Health Risk: Medium')
elif status == 'Normal':
    print('Recomendation: Maintain Weight')
    print('Health Risk: Low')
elif status == 'Overweight':
    print('Recomendation: Lose Weight')
    print('Health Risk: Medium')
elif status == 'Obese':
    print('Recomendation: Lose a lot of Weight')
    print('Health Risk: High')