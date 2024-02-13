yearly_basketball_training = int(input())

sneakers = yearly_basketball_training - (yearly_basketball_training * .40)
outfit = sneakers - (sneakers * .20)
basketball_ball = outfit * .25
basketball_accessories = basketball_ball * .20

final_price = sneakers + outfit + basketball_ball + basketball_accessories + yearly_basketball_training

print(final_price)