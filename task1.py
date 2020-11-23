import random

dirty = 0
perfomace = 0
for i in range(100):
    if random.randint(0, 1) == 1:
        dirty = dirty + 1
        if random.randint(0, 1) == 1:
            perfomace = perfomace + 1
        else:
            perfomace = perfomace - 1
print("Total dirty rooms: ", str(dirty))
print("Perfomance measure: ", str(perfomace))