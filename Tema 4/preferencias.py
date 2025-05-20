from nicegui import ui

# Función que muestra las preferencias seleccionadas
def mostrar():
    ui.notify(f'Color: {color.value}, Tema oscuro: {tema.value}')

# Crear un selector (select) con opciones de color:
color = ui.select(['Rojo', 'Verde', 'Azul'], label='Color favorito')

# Crear un switch para el tema oscuro:
tema = ui.switch('Tema oscuro')

# Crear botón para guardar preferencias:
ui.button('Guardar preferencias', on_click=mostrar)

# Iniciar la aplicación web
ui.run()