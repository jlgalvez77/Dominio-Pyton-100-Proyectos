# Proyecto 2, Saludo personalizado

nombre = input("Ingresa tu nombre: ")
nacimiento = int(input("Ingresa tu año de nacimiento(YYYY): "))
color = input("Ingresa tu color favorito: ")

ANIO_ACTUAL = 2025
edad = ANIO_ACTUAL - nacimiento

print('\n----- Saludo Personalizado -----')
print(f'Hola {nombre}, tienes {edad} años y tu color favorito es el: {color}')
print('Estás listo para comenzar tu aventura en Python')