# 10.10
class Laser:
    def does(self):
        return 'Disintegrate'


class Claw:
    def does(self):
        return 'Crush!'


class SmartPhone:
    def does(self):
        return 'Ring'


class Robot:
    def __init__(self):
        self.Laser = Laser()
        self.Claw = Claw()
        self.SmartPhone = SmartPhone()

    def does(self):
        print("Laser does: ", self.Laser.does())
        print("Claw does: ", self.Claw.does())
        print("Smartphone does: ", self.SmartPhone.does())


robot = Robot()
robot.does()
