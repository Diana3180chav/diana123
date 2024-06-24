import csv
with open('datos.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)# recorremos cada fila con un For
    for fila in lector_csv:
        nombre = fila['Nombre']
edad = int(fila['Edad'])
comuna = fila['Comuna']
estado_edad = "Mayor de Edad" if edad >= 18 else "Menor de Edad"
print(f"{nombre} tiene {edad} años, es {estado_edad} y vive en {comuna}")