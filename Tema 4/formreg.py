# Importar la biblioteca NiceGUI para crear interfaces web
from nicegui import ui
# Función que se ejecuta al hacer click en el botón de registro
def enviar():
    # Mostrar notificación con el nombre del usuario registrado
    ui.notify(f'Usuario {nombre.value} registrado con éxito')
# Crear campo de entrada para el nombre con etiqueta "Nombre"
nombre = ui.input(label='Nombre')
# Crear campo de entrada para el email con etiqueta "Email"
email = ui.input(label='Email')
# Crear campo de entrada para la contraseña:
contraseña = ui.input(label='Contraseña', password=True)
# Añadir casilla de verificación para aceptar términos y condiciones
ui.checkbox('Acepto los términos')
# Crear botón de registro:
ui.button('Registrarse', on_click=enviar)
# Iniciar la aplicación web
ui.run()