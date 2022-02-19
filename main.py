import random 


def frequenceAniversaire(nbrTentative, nbrDate):
    dates = []
    annivCommun = 0
    for i in range(nbrTentative):
        dates.clear()
        for k in range(nbrDate):
            dates.append(random.randint(1,365))
        if(len(dates)!= len(set(dates))):
           annivCommun = annivCommun + 1
    chance = annivCommun / nbrTentative
    return chance
    
