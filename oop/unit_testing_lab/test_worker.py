from unittest import TestCase, main

class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("TestWorker", 1000, 50)

    def test_correct_initialization(self):
        self.assertEqual("TestWorker", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_energy_is_incremented_after_rest(self):
        self.expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(self.expected_energy, self.worker.energy)

    def test_worker_when_energy_is_negative_or_zero(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_is_increased_and_energy_decreased_correctly_after_work(self):
        self.expected_money = self.worker.money + self.worker.salary
        self.expected_energy = self.worker.energy - 1
        self.worker.work()

        self.assertEqual(self.expected_money, self.worker.money)
        self.assertEqual(self.expected_energy, self.worker.energy)

    def test_if_get_info_returns_correct_string(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', self.worker.get_info())


if __name__ == "__main__":
    main()