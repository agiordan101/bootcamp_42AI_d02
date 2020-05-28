import time
from random import randint
from types import MethodType


begin_time = time.time()


def log(function):

    def function_modifed(*args, **kwargs):
        log_file = open("machine.log", 'a')
        log_file.write("Running: {: <20} [exec-time = {:.4} ms]\n".format(
                       function.__name__, (time.time() - begin_time) * 1000))
        if len(args) == 1:
            function(args[0])
        else:
            function(args[0], args[1])
        log_file.close()
    return function_modifed


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    log_file = open("machine.log", "w")
    log_file.write("")
    log_file.close()

    machine = CoffeeMachine()
    print(machine)
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
