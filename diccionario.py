personas = {'nombre': 'Rosa', 'edad':32, 'ciudad': 'Valencia'}

lista_personas =[ {'nombre': 'Rosa', 'edad':30, 'ciudad': 'Valencia' },
                  {'nombre': 'Pedro', 'edad':28, 'ciudad': 'Madrid' },
                  {'nombre': 'María', 'edad':50, 'ciudad': 'Cádiz' },
                  {'nombre': 'Raúl', 'edad':18, 'ciudad': 'Vitoria' }]




print(len(personas))
print(personas['nombre'])
print(personas['edad'])
print(personas['ciudad'])

personas['nombre'] = "Jose"
print(personas['nombre'])
print(personas.keys()) #obtengo todas las calves o keys
print(personas.values()) #obtengo todos los valores del diccionario
print(personas.items()) #obtengo valor y clave
print(personas.get('nombre')) #obtengo el valor por su key
print(personas.pop('edad')) #eliminar un elemento por su clave
print(personas)
print(personas.update({'pais': 'España'})) #añadir un elemento nuevo
print(personas)

for key, value in personas.items():
    print(f"key: {key}, value: {value}")
