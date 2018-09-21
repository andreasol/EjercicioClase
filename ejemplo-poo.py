clientes = [
    {'Nombre': 'Roberto', 'Apellidos': 'Noboa', 'dni': '0927231234'},
    {'Nombre': 'Nicolas', 'Apellidos': 'Noboa Burdett', 'dni': '09122121'},
    {'Nombre': 'Juan', 'Apellidos': 'García', 'dni': '09121213442'}
]


def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'], c['Apellidos']))
            return
    print('Cliente no encontrado')


def borrar_cliente(clientes, dni):
    for i, c in enumerate(clientes):
        if (dni == c['dni']):
            del (clientes[i])
            print(str(c), "> BORRADO")
            return
    print('Cliente no encontrado')

validador = mostrar_cliente(clientes,'09121213442')
print(validador)