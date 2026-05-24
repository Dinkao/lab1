import pytest
from lbibo import ElectricMotor
from newclass import VisionSystem
def test_create_motor():
    motor = ElectricMotor("A123", 250, 1500, 90, 380)
    assert motor.model == "A123"
    assert motor.power == 250
    assert motor.speed == 1500
    assert motor.efficiency == 90
    assert motor.voltage == 380

def test_power_validation():
    motor = ElectricMotor("Test", 250, 1000, 85, 220)
    motor.power = 150
    assert motor.power == 250
    motor.power = 350
    assert motor.power == 250
    motor.power = 270
    assert motor.power == 270 

def test_current_property():
    motor = ElectricMotor("Test", 250, 1000, 85, 220)
    expected_current = 250 / (220 * 85)
    assert abs(motor._calc_current() - expected_current) < 0.01
    
    motor.power = 270
    expected_current = 270 / (220 * 85)
    assert abs(motor._calc_current() - expected_current) < 0.01

def test_eq_method():
    motor1 = ElectricMotor("XYZ123", 250, 1500, 90, 380)
    motor2 = ElectricMotor("XYZ123", 270, 2000, 88, 220)
    motor3 = ElectricMotor("ABC456", 250, 1500, 90, 380)
    
    assert motor1 == motor2
    assert motor1 != motor3
    assert motor1 != "not a motor"

def test_lt_method():
    motorS = ElectricMotor("Small", 220, 1500, 90, 380)
    motorM = ElectricMotor("Medium", 250, 1500, 90, 380)
    motorL = ElectricMotor("Large", 280, 1500, 90, 380)
    
    assert (motorS < motorM) == True
    assert (motorM < motorL) == True
    assert (motorL < motorM) == False
    assert (motorM < motorS) == False
    assert (motorS < "палец") == False

def test_add_method():
    motor1 = ElectricMotor("A", 250, 1000, 85, 220)
    motor2 = ElectricMotor("B", 270, 1500, 90, 380)
    motor_sum = motor1 + motor2
    
    assert isinstance(motor_sum, ElectricMotor)
    assert motor_sum.model == "A"
    assert motor_sum.power == 520
    assert motor_sum.speed == 2500
    assert motor_sum.efficiency == 175
    assert motor_sum.voltage == 600

def test_init():
    device = VisionSystem("SVG", 800, 350, 240, 500)
    assert device.model == "SVG"
    assert device.resolution == 800
    assert device.sensor_type == 350
    assert device.frame_rate == 240
    assert device.interface == 500    