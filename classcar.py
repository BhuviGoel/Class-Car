class Car:
    def __init__(self, speed, color, brand):
        self.speed = speed
        self.color = color
        self. brand = brand

    def start(self):
        print("the " + self.color + "car has started to move with a speed of", self.speed)  
    def stop(self):
        print("the "+ self.brand +" car has stopped moving")                
car1 = Car(20, "blue", "BMW")
car1.start()
car1.stop()