from project.car import Car


class FamilyCar(Car):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        if self.fuel_consumption * kilometers <= self.fuel:
            self.fuel -= self.fuel_consumption * kilometers


