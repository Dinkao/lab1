print("Привет")
import json
import csv
import random
from random import randint
from newclass import BaseDevice
class ElectricMotor(BaseDevice):
    def __init__(self, model, power, speed, efficiency, voltage):
        super().__init__(model)
        self.__model = model
        self.__power = power
        self.__speed = speed
        self.__efficiency = efficiency
        self.__voltage = voltage
        self.__current = self._calc_current()
       
    def info(self):
        return f"Двигатель {self.__model}:{self.__power} КВт, {self.__speed} об/мин, {self.__efficiency} КПД, {self.__voltage} В, {self.__current}"
    @property
    def model(self):
        return self.__model
    @property
    def power(self):
        return self.__power
    @power.setter
    def power(self, power):
     if  200 < power < 300:
         self.__power = power
         self.__current = self._calc_current()
     else:
            
            print("Недопустимая мощность")    
    @property
    def speed(self):
        return self.__speed     
    @property
    def efficiency(self):
        return self.__efficiency
    @property
    def voltage(self): 
        return self.__voltage
    def _calc_current(self): 
     
        return    self.__power/(self.__voltage*self.__efficiency)
    def __repr__(self):
        return f"ElectricMotor('{self.__model}',{self.__power},{self.__speed},{self.__efficiency},{self.__voltage},{self.__current})"
    def __str__(self):
        return f"Двигатель {self.__model}:{self.__power} КВт, {self.__speed} об/мин, {self.__efficiency} КПД, {self.__voltage} В, {self.__current}"
    def __eq__(self, other):
        if not isinstance(other,ElectricMotor): return NotImplemented
        return self.model == other.model
        
    def __lt__(self, other):
        if isinstance(other,ElectricMotor):
            return self.__power < other.__power
        return False
    def __add__(self, other):
        if not isinstance(other,ElectricMotor): return NotImplemented
        
        return ElectricMotor(self.model, self.power + other.power, self.speed + other.speed, self.efficiency + other.efficiency, self.voltage + other.voltage)
    def __sub__(self, other):
         if isinstance(other,ElectricMotor):
             return ElectricMotor(self.model, self.power - other.power, self.speed - other.speed, self.efficiency - other.efficiency, self.voltage - other.voltage)
    data = [{"time":"2025-20-20 10:00","power": 220,"speed": 300}]
    with open("electric_log.csv", "w", newline=4, encoding="utf-8")as f:
        fieldnames = ["model", "power", "speed", "efficiency", "voltage", "current"]       
        writer =  csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print("CSV сохранен")
    with open("electric_log.csv", "r", encoding="utf-8")as f:   
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("JSON сохранен")
    csv_data = []
    with open("electric_log.csv", "r", encoding="utf-8")as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["power"] = int(row["power"])
            row["voltage"] = float(row["voltage"])
            row["model"] = int(row["model"])
            row["speed"] = int(row["speed"])
            csv_data.append(row)
    print("Из CSV прочитано:", csv_data)
    with open("electric_log.json", "r", encoding="utf-8")as f:
        json_data = json.load(f)
    print("из JSON прочитано:", json_data)            
def generate_test_data(cls,count,**kwargs):
    result = []
    models=["Diana","umnica"]
    power= (200,300)
    speed=(1,9)
    efficiency = (1000,9999)
    voltage = (10,99)
    for item in kwargs:
        if item =="models":
            models=kwargs[item]
        if item == "power":
            power=kwargs[item]
        if item == "speed":
            speed=kwargs[item]
        if item == "voltage":
            voltage=kwargs[item]
        if item == "efficiency":
            efficiency=kwargs[item]

    # models = ["SPR", "SPE", "GSV", "SGA", "FDG"]
    
    for i in range(count):
        curent_model=random.choice(models)
        cur_power=random.randint(power[0],power[1])
        cur_speed=random.randint(speed[0],speed[1])
        cur_vol=random.randint(voltage[0],voltage[1])
        cur_efc=random.randint(efficiency[0],efficiency[1])
        motor=cls(curent_model,cur_power,cur_speed,cur_efc,cur_vol)
        result.append(motor)
    return result

   

print(generate_test_data(ElectricMotor,10))
  



        

                              




