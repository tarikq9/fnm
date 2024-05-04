#BreakEvenPoint lineare

import numpy as np
import matplotlib.pyplot as plt
import math as m

#Test dati
cf=90000     #costi fissi
cvu=200      #costi variabili unitari
ru=500       #ricavi unitari

def bep(tempo):
    q=cf/(ru-cvu)
    ore=tempo*q
    print("la quantità di bep arrotondata è di:",m.ceil(q))
    print("i ricavi per il bep sono di :",round(ru*q,2))
    print('il bep sarà raggiunto con un ammontare di ore pari a',ore)
    
    #Grafico  
    x=np.linspace(0,q*2,100)     #asse x
    y1=ru*x                        #retta ricavi totali
    y2=cvu*x                       #retta costi variabili
    y3=y2+cf                       #retta costi totali
    
    plt.hlines(y=cf,xmin=0,xmax=q*2,color="black",linestyles="-",label="costi fissi") #retta costi fissi 
    plt.hlines(y=q*ru,xmin=0,xmax=q,color="blue",linestyle="--",alpha=0.5)
    plt.vlines(x=q,ymin=0,ymax=q*ru,color="blue",linestyle="--",alpha=0.5)
    
    plt.plot(x,y1,label="ricavi totali")
    plt.plot(x,y2,label="costi variabili",color='green')
    plt.plot(x,y3,label="costi totali",color='purple')
    plt.fill_between(x,y1, y3,where = y1>=y3,facecolor ='green', alpha = 0.3)
    plt.fill_between(x,y1,y3,where= y1<=y3,facecolor = "red",alpha=0.3)
    plt.plot(q,q*ru,"bo",label="break even point")
    
    plt.xlabel("QUANTITA DA VENDERE")
    plt.ylabel("COSTI E RICAVI")
    plt.grid(linestyle='--',linewidth=0.5)
    plt.margins(0)
    plt.legend()
    plt.title("BREAK EVEN POINT")
    plt.show()   
bep(32/60) #tempo medio per produrre 1 unità, espresso in ore
