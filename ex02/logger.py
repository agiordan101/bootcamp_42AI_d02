import time
from random import randint
from types import MethodType
import os


def log(function):

    def function_modifed(*args, **kwargs):
        log_file = open("machine.log", 'a')
        begin_time = time.time()
        if len(args) == 1:
            ret = function(args[0])
        else:
            ret = function(args[0], args[1])
        dtime = time.time() - begin_time
        log_file.write("({})Running: {: <15} [exec-time = "
                       .format(os.environ["USER"], function.__name__))
        if dtime > 1:
            log_file.write("{: <6.2} s]\n".format(dtime))
        else:
            log_file.write("{: <6.2} ms]\n".format(dtime * 1000))
        log_file.close()
        return (ret)
    return function_modifed


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        print("Water lvl {}".format(self.water_level))
        if self.water_level > 20:
            print("Start machine !")
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
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
