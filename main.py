
from lbibo import ElectricMotor
motor = ElectricMotor("SOM524",270,300,85,220)
print(motor.info())
motor.power = 204
motor1 = ElectricMotor("SSM2244",200,320,85,220)
motor2 = ElectricMotor("SPM254",280,300,85,220)
motor.info()
print(motor.info())
print(motor1.info())
print(motor2.info())
print (motor.__str__())
#motor3 = eval(repr(ElectricMotor))
motor3 = motor1.__repr__()
motor4 = motor1 + motor2
print(motor4)
motor5 = motor4 - motor1
print(motor5)