#BreakEvenPoint lineare

import numpy as np
import matplotlib.pyplot as plt
import math as m

#Test dati
cf=35000     #costi fissi
cvu=150      #costi variabili unitari
ru=250       #ricavi unitari

def bep(tempo):
    q=cf/(ru-cvu)
    ore=tempo*q
    print("la quantità di bep arrotondata è di:",m.ceil(q))
    print("i ricavi per il bep sono di :",round(ru*q,2))
    print('il bep sarà raggiunto con un ammontare di ore pari a',ore)
    
    #Grafico  
    fig, ax = plt.subplots()
    x=np.linspace(0,q*2,100)     
    y1=ru*x                        #retta ricavi totali
    y2=cvu*x                       #retta costi variabili
    y3=y2+cf                       #retta costi totali
    
    plt.hlines(y=cf,xmin=0,xmax=q*2,color="darkmagenta",linestyles="-",label="costi fissi") #retta costi fissi 
    plt.hlines(y=q*ru,xmin=0,xmax=q,color="olive",linestyle="--",alpha=0.5)
    plt.vlines(x=q,ymin=0,ymax=q*ru,color="olive",linestyle="--",alpha=0.5)
    
    
    plt.plot(x,y2,label="costi variabili",color='darkorange')
    plt.plot(x,y3,label="costi totali",color='crimson')
    plt.plot(x,y1,label="ricavi totali",color='darkblue')
    plt.fill_between(x,y1, y3,where = y1>=y3,facecolor ='seagreen', alpha = 0.25)
    plt.fill_between(x,y1,y3,where= y1<=y3,facecolor = "firebrick",alpha=0.3)
    plt.plot(q,q*ru,"yo",label="break even point")
    
    plt.xlabel("QUANTITA DA VENDERE")
    plt.ylabel("COSTI E RICAVI")
    plt.margins(0)
    plt.legend()
    plt.title("BREAK EVEN POINT")
    ax.set_facecolor('floralwhite')
    plt.show()   
bep(30/60) #tempo medio per produrre 1 unità, espresso in ore
