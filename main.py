import random 


def frequenceAniversaire(nbrTentative, nbrPersonnes):
    dates = []
    annivCommun = 0
    for i in range(nbrTentative):
        dates.clear()
        for k in range(nbrPersonnes):
            dates.append(random.randint(1,365))
        if(len(dates)!= len(set(dates))):
           annivCommun = annivCommun + 1
    chance = annivCommun / nbrTentative
    return chance
