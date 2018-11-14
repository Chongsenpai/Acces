import random

def importList(file):
    f = open(file)
    output = f.readlines()
    f.close()
    for i in range(len(output)):
        output[i] = output[i].strip()
    return output

adj = importList("Adjektiver.txt")
sub = importList("Substantiver.txt")

def getRandom(list):
    rand = random.choice(list)
    return rand

def makeAttack():
    atk = str(getRandom(adj)) + " " + str(getRandom(sub)) + "!"
    return atk

