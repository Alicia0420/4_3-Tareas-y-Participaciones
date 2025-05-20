from nicegui import ui

# Título
ui.label('Calculadora Básica').classes('text-h4')

# Entradas de número
num1 = ui.number(label='Número 1', value=0)
num2 = ui.number(label='Número 2', value=0)

# Resultado
resultado = ui.label('Resultado: 0').classes('text-h6')

# Funciones de operación
def calcular_suma():
    suma = num1.value + num2.value
    resultado.text = f'Resultado: {suma}'
    ui.notify(f'La suma es {suma}')

def calcular_resta():
    resta = num1.value - num2.value
    resultado.text = f'Resultado: {resta}'
    ui.notify(f'La resta es {resta}')

def calcular_multiplicacion():
    multiplicacion = num1.value * num2.value
    resultado.text = f'Resultado: {multiplicacion}'
    ui.notify(f'La multiplicación es {multiplicacion}')

def calcular_division():
    if num2.value != 0:
        division = num1.value / num2.value
        resultado.text = f'Resultado: {division}'
        ui.notify(f'La división es {division}')
    else:
        resultado.text = 'Resultado: Error (división por cero)'
        ui.notify('No se puede dividir entre cero')

# Botones para cada operación
ui.button('Sumar', on_click=calcular_suma)
ui.button('Restar', on_click=calcular_resta)
ui.button('Multiplicar', on_click=calcular_multiplicacion)
ui.button('Dividir', on_click=calcular_division)

# Ejecutar la app
ui.run()