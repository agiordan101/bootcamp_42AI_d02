import math


class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, values):
        if len(values) == 0:
            return None
        else:
            return sum(values) / len(values)

    def quartiles(self, values, percent):
        values.sort()
        length = len(values)
        i_max = percent * length / 100
        if length == 0:
            return None
        for i in range(length):
            if (i > i_max):
                return values[i - 1]
        return values[-1]

    def median(self, values):
        return self.quartiles(values, 50)

    def var(self, values):
        average = self.mean(values)
        deviation = []
        for value in values:
            deviation.append(value - average)
            deviation[-1] *= deviation[-1]
        return self.mean(deviation)

    def std(self, values):
        return math.sqrt(self.var(values))


stats = TinyStatistician()
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(stats.mean(values))
print(stats.median(values))
print(stats.quartiles(values, 0))
print(stats.quartiles(values, 10))
print(stats.quartiles(values, 25))
print(stats.quartiles(values, 100))
print(stats.var(values))
print(stats.std(values))
print()
values = [1, 42, 300, 10, 59]
print(stats.mean(values))
print(stats.median(values))
print(stats.quartiles(values, 25))
print(stats.quartiles(values, 75))
print(stats.var(values))
print(stats.std(values))
