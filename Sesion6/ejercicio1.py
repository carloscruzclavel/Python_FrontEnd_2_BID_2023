""" u1 = {
    'id':1,
    'usuario':'alicia',
    'correo':'alicia@gmail.com',
    'token':'sadasdsasfsadasdajsdusagdsajkas',
    'rol':{1: 'admin', 2: 'gerente'},
}
u2 = {
    'id':2,
    'usuario':'beto',
    'correo':'beto@gmail.com',
    'token':'asdkjsadlsadjnsakndskamdska',
    'rol':{3: 'VEntas', 4: 'user',5: 'rrhh'},
}
Lista_usuarios = []
Lista_usuarios.append(u1)
Lista_usuarios.append(u2)

print(Lista_usuarios[1]['correo'])
print(Lista_usuarios[0]['rol'][1])


for valor in Lista_usuarios[1]['rol'].values():
    print(f'Valor:{valor}') """



""" opcs = input('Ingrese la opción que desea:')

if(opcs == '1'):
    d1 = input('ingrese el nombre del empleado:')
    d2 = input('Ingrese el cargo del empleado:')
    d3 = int(input('Ingrese el sueldo del empleado:'))
    print('Registro guardado')
    datos = {
    'nombre:':d1,
    'cargo': d2,
    'sueldo' : d3,
    }

    lista = []
    lista.append(datos)
if(opcs == '2'):
    for valor in lista[0].values():
        print(f'{valor}')
 """

while True:
    print('Seleccione una opción del menú:')
    print('1. Agregar Empleado')
    print('2. Imprimir Lista')
    print('3. Salir')
    opcion = int
    if opcion in [1,2,3]:
        print('Intento 1')
print('nuevo')
    








