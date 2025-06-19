# Proyecto 3, calculadora simple

print('----- Calculadora -----')
num1 = float(input('Ingresa el primer numero: '))
num2 = float(input('Ingresa el segundo numero: '))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
divivision = num1 / num2 if num2 != 0 else 'No se puede dividir por cero'

print(f'La suma es: {suma}')
print(f'La resta es: {resta}')
print(f'La multiplicacion es: {multiplicacion}')
print(f'La division es: {divivision}')