from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan

class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription_plan = next(s for s in self.subscriptions if s.id == subscription_id)
        equipment_id = next(e.equipment_id for e in self.plans if e.trainer_id == subscription_plan.trainer_id)
        customer = next(c.__repr__() for c in self.customers if c.id == subscription_plan.customer_id)
        trainer = next(t for t in self.trainers if t.id == subscription_plan.trainer_id)
        equipment = next(e for e in self.equipment if e.id == equipment_id)
        plan = next(p.__repr__() for p in self.plans if p.id == subscription_plan.exercise_id)
        return f"{subscription_plan.__repr__()}\n{customer}\n{trainer.__repr__()}\n{equipment}\n{plan}"
