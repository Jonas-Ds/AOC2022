import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input_day4.txt','r') as f:
    content = f.read().split("\n")
    del content[-1]
    counter = 0
    for line in content:
        FirstElf , SecondElf = line.split(",")
        FirstElfStart , FirstElfStop = FirstElf.split('-')
        SecondElfStart , SecondElfStop = SecondElf.split('-')
        if (FirstElfStart <= SecondElfStart) and (FirstElfStop>= SecondElfStop):
            counter +=1
        if (SecondElfStart <= FirstElfStart) and (SecondElfStop >= FirstElfStop):
            counter += 1
        print(counter, FirstElf, SecondElf)
    