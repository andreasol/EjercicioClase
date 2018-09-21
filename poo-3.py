class Motor:
    fabricante = ''

    def __init__(self, fabricante=''):
        self.fabricante = fabricante

    def start(self):
        print('ARRANCA')

    def stop(self):
        print('STOP')

    def __str__(self):
        return self.fabricante

class MotorElectrico(Motor):  # Is-A Motor
    marca = ''

    def __init__(self, marca=''):
        super(Motor).__init__()
        self.marca = marca

    def __str__(self):
        return self.marca

   # def start(self):
    #
        print('Arranca el motor electrico')

class V8Motor(Motor):  # Is-A Motor
    pass

class Car:
    motor_class = Motor

    def __init__(self):
        self.motor = self.motor_class  # Has-A Motor

    def start(self):
        print(
            'Enciende el motor {0} del carro {1}..!'
                .format(
                self.motor.__class__.__name__,
                self.__class__.__name__)
        )
        self.motor.start()

    def stop(self):
        self.motor.stop()


motor = Motor(fabricante='BOSCH')
motore1 = MotorElectrico(marca='demo')
motore1.start()