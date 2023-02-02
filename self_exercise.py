# 10.9
class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


bear1 = Bear()
rabbit1 = Rabbit()
octo1 = Octothorpe()

print("Bear eats:", bear1.eats())
print("Rabbit eats:", rabbit1.eats())
print("Octothorpe eats:", octo1.eats())
