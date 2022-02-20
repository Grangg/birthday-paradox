import random
import matplotlib.pyplot as plt 


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
    

def frequenceAniversaireGraph(nbrTentative, nbrPersonnesMax):
    dates = []
    annivCommun = 0
    
    xValues = []
    yValues = []
    
    for v in range(nbrPersonnesMax):
        annivCommun = 0
        for i in range(nbrTentative):
            dates.clear()
            for k in range(v):
                dates.append(random.randint(1,365))
            if(len(dates)!= len(set(dates))):
               annivCommun = annivCommun + 1
        chance = (annivCommun / nbrTentative)*100
        xValues.append(v)
        yValues.append(chance)
    plt.plot(xValues,yValues)
    plt.xlabel('Nombre de personne')
    plt.ylabel('Pourcentage de chance d\'avoir une date d\'anniversaire commune')
    plt.axis([0, v, 0, 100])
    plt.show()
