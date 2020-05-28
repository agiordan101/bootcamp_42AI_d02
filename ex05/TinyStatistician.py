class TinyStatistician:
    def __init__(self):
        pass
    
    def mean(self, values):
        if len(values) == 0:
            return None
        else:
            return sum(values) / len(values)
    
    def median(self, values, percent):
        length = len(feature)
        for i in range(length):
            if (i > percent * length):
                if (i == 1):
                    return values[0]
                else:
                    return values[i - 2]
        return values