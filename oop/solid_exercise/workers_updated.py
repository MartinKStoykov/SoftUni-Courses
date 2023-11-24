from abc import ABCMeta, abstractmethod, ABC
import time

class Workable(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass

class Eatable(ABC):
    @staticmethod
    @abstractmethod
    def eat():
        pass

class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)

class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)
class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")
class BaseManager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass

    @abstractmethod
    def manage(self):
        pass

class WorkManager(BaseManager):

    def __init__(self):
        super().__init__()

    def set_worker(self, worker):
        assert isinstance(worker, Workable), "`worker` must be of type {}".format(Workable)

        self.worker = worker

    def manage(self):
        self.worker.work()

class BreakManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Eatable), "`worker` must be of type {}".format(Eatable)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()
