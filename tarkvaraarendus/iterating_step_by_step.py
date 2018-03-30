def main():
    GetARangeOfNumber()
def GetARangeOfNumber():
    for index in IteratingStepByStep(1,123, 7):
        print(index, end=' ')
def IteratingStepByStep(start, stop, step):
    number = start
    while number <= stop:
        yield number
        number += step
main()