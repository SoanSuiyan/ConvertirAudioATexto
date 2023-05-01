import os
from voz import Recibir_audio as ra

ruta_guardado = input('Ingrese la ruta de guardado (dejar en blanco para guardar en la carpeta por defecto): ')

if ruta_guardado == '':
    # Si no se ingresó ninguna ruta, utilizar la ruta por defecto
    ruta_guardado = os.path.join(os.path.expanduser("~"), "Documents", "bloosverd")
    # Verificar si la ruta existe, si no existe, crear la carpeta
    if not os.path.exists(ruta_guardado):
        os.makedirs(ruta_guardado)

nombre_archivo = input('Ingrese el nombre del archivo: ')
nombre_archivo_txt = nombre_archivo + '.txt'  # Agregar la extensión .txt al nombre del archivo

archivo_listo = os.path.join(ruta_guardado, nombre_archivo_txt)  # Usar os.path.join para crear la ruta completa

if os.path.exists(archivo_listo):
    print(f'El archivo {nombre_archivo_txt} ya existe en la siguiente dirección\n{archivo_listo}')
    respuesta = input('¿Desea agregar contenido al archivo existente? (s/n): ')
    if respuesta.lower() == 's':
        with open(archivo_listo, 'a') as archivo:
            contenido = ra() #input('Ingrese el contenido a agregar: ')
            archivo.write(contenido)
    else:
        print('No se agregó contenido al archivo existente.')
else:

    with open(archivo_listo, 'w') as archivo:
        contenido = ra() #input('Ingrese el contenido del archivo: ')
        archivo.write(contenido)
        print(f'el archivo se guardó correctamente en la siguiente dirección:\n{archivo_listo}')