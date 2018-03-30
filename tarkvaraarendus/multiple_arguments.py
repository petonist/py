def AnotherRangeOfArguments(*args):
    numberOfArguments = len(args)

    if numberOfArguments < 1: raise TypeError('vähemalt ühte argumenti on vaja')
    elif numberOfArguments == 1: 
        stop = args[0]        #kui üks argument siis võetakse seda stopina
        start = 0
        step = 1
    elif numberOfArguments == 2:
        (start, stop) = args
        step = 1
    elif numberOfArguments == 3:
        (start, stop, step) = args

    i = start
    while i <= stop:
        yield i
        i += step

for index in AnotherRangeOfArguments(7):
    print(index, end=' ')