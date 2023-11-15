#BreakEvenPoint lineare
import numpy as np
import matplotlib.pyplot as plt
import math

#Inserire nella funzione fx rispettivamente i costi fissi, costi variabili u e i ricavi unitari, riga 40
def fx(cf,cvu,ru):
    q=cf/(ru-cvu)
    
    
    #Grafico  
    x=np.array([0,q*0.4,q*0.8,q,q*1.2,q*1.6])                                           #asse x
    y1=np.array([0,ru*q*0.4,ru*q*0.8,ru*q,ru*q*1.2,ru*q*1.6])                           #retta ricavi totali
    y2=np.array([cf,q*0.4*cvu+cf,q*0.8*cvu+cf,q*cvu+cf,q*1.2*cvu+cf,q*1.6*cvu+cf])      #retta costi totali
    y3=np.array([0,q*0.4*cvu,q*0.8*cvu,q*cvu,q*1.2*cvu,q*1.6*cvu])
    
    plt.hlines(y=cf,xmin=0,xmax=q*1.6,color="black",linestyles="-",label="costi fissi") #retta costi fissi 
    plt.hlines(y=q*ru,xmin=0,xmax=q,color="blue",linestyle="--",alpha=0.5)
    plt.vlines(x=q,ymin=0,ymax=q*ru,color="blue",linestyle="--",alpha=0.5)
    
    print("la quantità di bep arrotondata è di:",math.ceil(q))
    print("i ricavi per il bep sono di :",round(ru*q,2))

    plt.plot(x,y1,label="ricavi totali")
    plt.plot(x,y2,label="costi totali")
    plt.plot(x,y3,label="costi variabili")
    plt.fill_between(x,y1, y2,where = y1>=y2,
                facecolor ='green', alpha = 0.4,)
    plt.fill_between(x,y1,y2,where= y1<=y2,
                     facecolor = "red",alpha=0.4)
    plt.plot(q,q*ru,"bo",label="break even point")
    
    plt.xlabel("QUANTITA'VENDUTE")
    plt.ylabel("COSTI E RICAVI")
    plt.grid(linestyle='--',linewidth=0.5)
    plt.margins(0)
    plt.legend()
    plt.title("BREAK EVEN POINT")
    plt.show()   
fx(8000,65,115)    