#BreakEvenPoint lineare

import numpy as np
import matplotlib.pyplot as plt
import math as m


cf=10000     #costi fissi
cvu=40      #costi variabili unitari
ru=95      #ricavi unitari

q=cf/(ru-cvu)
print("la quantità di bep arrotondata è di:",m.ceil(q))
print("i ricavi per il bep sono di :",round(ru*q,2))
   
#Grafico  
x=np.linspace(0,q*1.6)           #asse x
y1=ru*x                          #retta ricavi totali
y2=cvu*x+cf                      #retta costi totali
y3=cvu*x                         #retta costi variabili
    
plt.hlines(y=cf,xmin=0,xmax=q*1.6,color="black",linestyles="-",label="costi fissi") #retta costi fissi 
plt.hlines(y=q*ru,xmin=0,xmax=q,color="blue",linestyle="--",alpha=0.5)
plt.vlines(x=q,ymin=0,ymax=q*ru,color="blue",linestyle="--",alpha=0.5)
    
plt.plot(x,y1,label="ricavi totali")
plt.plot(x,y2,label="costi totali")
plt.plot(x,y3,label="costi variabili")
plt.fill_between(x,y1, y2,where = y1>=y2,facecolor ='green', alpha = 0.4,)
plt.fill_between(x,y1,y2,where= y1<=y2,facecolor = "red",alpha=0.4)
plt.plot(q,q*ru,"bo",label="break even point")
    
plt.xlabel("QUANTITA'VENDUTE")
plt.ylabel("COSTI E RICAVI")
plt.grid(linestyle='--',linewidth=0.5)
plt.margins(0)
plt.legend()
plt.title("BREAK EVEN POINT")
plt.show()   