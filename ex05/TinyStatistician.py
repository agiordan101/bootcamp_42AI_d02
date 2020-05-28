class TinyStatistician:
    def __init__(self):
        pass
    
    def mean(self, values):
        if len(values) == 0:
            average = None
        else:
            average = 0
        for value in values:
            average +=