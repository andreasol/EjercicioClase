
class Cliente:
    dni = ''
    nombres = ''
    apellidos = ''

    def __init__(self, dni=None, nombres = '', apellidos = ''): #Definiendo el metodo constructor de la clase cliente
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos

    def __str__(self):
        return f"Cliente: {self.dni} - {self.nombres}"


class Empresa:
    nombre=''

    def __init__(self, nombre='', clientes=[]):
        self.nombre = nombre
        self.clientes = clientes

    def __str__(self):
        return self.nombre

    def mostrar_clientes(self,clientes):
        for c in clientes:
            print(f"Cliente: {c}")

    @staticmethod
    def metodo_2(p1=''):
        #print('Imprimiendo cls:', cls)
        return pl


clientes = []
c1 = Cliente(dni='123123123', nombres='Andrea', apellidos='Freire')
c2 = Cliente(dni='123432123', nombres='Andres', apellidos='Burdeos')
c3 = Cliente(dni='123432124', nombres='Juan', apellidos='Alvarado')
clientes.append(c1)
clientes.append(c2)
clientes.append(c3)
for item in clientes:
    print(f"Cliente: {item.nombres} - {item.apellidos} - {item.dni}")
print(c1)
print(c1.nombres)
empresa = Empresa(nombre='Empresa1', clientes=clientes)
print (empresa)
print(empresa.mostrar_clientes(clientes)) # aqui sale el none
empresa.mostrar_clientes(clientes)
#Empresa.mostrar_clientes(clientes) # muestra excepcion