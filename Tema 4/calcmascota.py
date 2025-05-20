from nicegui import ui
# Función que calcula la edad canina basada en la edad humana
def calcular():
    # Convertir el valor del input a entero y multiplicar por 7
    edad_mascota = int(humano.value) * 7
    # Actualizar el texto del label con el resultado del cálculo
    resultado.set_text(f'Edad estimada en años perrunos: {edad_mascota}')
humano = ui.input(label='Edad humana').props('type=number')

# Crear botón de cálculo:
ui.button('Calcular edad de mascota', on_click=calcular)

# Crear elemento label para mostrar el resultado
resultado = ui.label()

# Iniciar la aplicación web
ui.run()