
class BaseDevice():
    def __init__(self,model):
        self.__model = model
    @property
    def model(self):
        return self.__model
    
class VisionSystem(BaseDevice):
    def __init__(self, model, resolution, sensor_type, frame_rate, interface):
        super().__init__(model)
        self.__model = model
        self.__resolution = resolution
        self.__sensor_type = sensor_type
        self.__frame_rate = frame_rate
        self.__interface = interface
        self.pixel_clock_ = self.pixel_clock()
    def info(self):
        return f"Визуальная система {self.__model}: {self.__resolution}: {self.__sensor_type}, {self.__frame_rate}: fps, {self.__interface}: classic"
    @property
    def model(self):
        return self.__model
    @property
    def resolution(self):
        return self.__resolution
    @resolution.setter
    def resolution(self, resolution):
     if  720 < resolution < 2000:
         self.resolution = resolution
     else:
         print("Недопустимое разрешение")
    @property
    def sensor_type(self):
        return self.__sensor_type
    @property
    def frame_rate(self):
        return self.frame_rate
    @property
    def interface(self):
        return self.interface
    def pixel_clock(self):
        return self.__resolution*self.frame_rate*10^6
    def __str__(self):
        return f"Визуальная система:{self.__model},{self.resolution}, {self.sensor_type} , {self.frame_rate} fps, {self.interface} classic"      
    def __repr__(self):
        return f"Визуальная система:{self.__model},{self.resolution}, {self.sensor_type}, {self.frame_rate}, {self.interface}"
    def __eq__(self,other):
        if not isinstance(other,VisionSystem) :  return NotImplemented
        return self.frame_rate == other.frame_rate
    def __lt__(self, other):
        if isinstance(other,VisionSystem):
            return self.resolution < other.resolution
        return False

        
