entered_height = int(input('enter height'))
entered_weight = int(input('enter weight'))
height = entered_height if entered_height >= 0 else print('enter proper value')
weight = entered_weight if entered_weight >= 0 else print('enter proper value')
BMI = (weight/(height^2))*703
status = ('Underweight' if BMI < 18.5 else
          "Normal" if 18.5<=BMI<25 else
          "Overweight" if 25<=BMI<30 else
          "Obese" if BMI >= 30 else
          'error')
print(status)