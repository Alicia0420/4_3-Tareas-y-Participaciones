from nicegui import ui
datos = [
    {'Nombre': 'Ana', 'Edad': 21},
    {'Nombre': 'Luis', 'Edad': 23},
    {'Nombre': 'Carla', 'Edad': 22},
]
ui.table(
    columns=[
        {'name': 'Nombre', 'label': 'Nombre', 'field': 'Nombre'},
        {'name': 'Edad', 'label': 'Edad', 'field': 'Edad'}
    ],
    rows=datos,
    row_key='Nombre'
)
ui.run()