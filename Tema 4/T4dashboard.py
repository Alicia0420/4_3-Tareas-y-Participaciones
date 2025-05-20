# Importar la biblioteca NiceGUI para crear interfaces web
from nicegui import ui

# Crear un diseño en fila (horizontal) para organizar los elementos
with ui.row():
    
    # Tarjeta principal para las ventas
    with ui.card():
        ui.label('Ventas')   
        ui.label(' $1,200')        
        
        # Tarjeta anidada para usuarios dentro de la tarjeta de ventas
        with ui.card():
            ui.label('Usuarios')   
            ui.label(' 342')      
            
            # Tarjeta doblemente anidada para tickets
            with ui.card():
                ui.label('Tickets') 
                ui.label(' 18')    

# Iniciar la aplicación web
ui.run()