#LEGENDA, inserire i valori in basso

n=30              # Anni o Rate
k=1               # k versamenti all'anno
i=0.03            # Tasso d'interesse ANNUO 
s=100000          # Debito iniziale
v=1               # v=1 se n in anni, v=k se n in rate 
 

def ammortamento(tipo) :
    #Importo le librerie necessarie 
    import math
    import numpy as np
    import pandas as pd 
    import matplotlib.pyplot as plt
    from tabulate import tabulate
    
    #Rispettivamente : nk= rate del piano , t= iterazione temporale , ik= tasso equivalente 
    nk= math.trunc(n*k/v)                               
    t= np.arange(1,nk+1)                                        
    ik= (1+i)**(1/k)-1                        
                              
    #Colonne R,QC,I,DR,DE
    if tipo=='francese':
        R= np.full(nk,s/((1-(1+ik)**-nk)/ik))
        QC= R*((1+ik)**-(nk-t+1))
        I=  R*((1-(1+ik)**-(nk-t+1)))
        DR= R*((1-(1+ik)**(-nk+t))/ik)
        DE= s-DR
    elif tipo=='italiano':
        QC= np.full(nk,(s/nk))
        DR= ((nk-t)/nk)*s
        DE= t*(s/nk)
        I= (nk-t+1)*(s/nk)*ik
        R=  QC+I


    #Creazione tabella 
    T=pd.DataFrame(zip(t,R,QC,I,DR,DE),
    columns=["N°Rate","Rata","Quote Capitale","Interessi","Debito Residuo","Debito Estinto"])
    

    #Stampa tabella e risultati 
    print(tabulate(T,headers="keys",tablefmt="fancy_grid",floatfmt=[".0f", ".2f", ".2f", ".2f", ".2f", ".2f"],showindex="never"))
    print("Totale Interessi:",round(sum(I),2))
    print("Importo totale da restituire: ",round(s+sum(I),2))
    print("Incidenza degli interessi sul capitale :",round(100*(sum(I))/(s),2),'%')


    #Stampa il grafico : andamento e incidenza interessi rispetto al capitale prestato
    fig, ax=plt.subplots()
    cumulativeI= np.cumsum(I)
    plt.plot(t,cumulativeI, label='curva interessi',color='firebrick',linestyle='--')
    plt.hlines(y=s,xmin=0,xmax=nk,color="darkgreen",linestyles="-",label="Debito iniziale")
    plt.hlines(y=s+(round(sum(I),2)),xmin=0,xmax=nk,color="darkblue",linestyles="-",label="Debito finale")
    
   
    plt.xlabel("RATE")
    plt.ylabel('Euro')
    plt.grid(linestyle='--',linewidth=0.5)
    plt.legend(ncol=4,loc='center',bbox_to_anchor=(0.5,1.06))
    ax.set_facecolor('floralwhite')
    plt.show()
ammortamento('francese') #inserire la tipologia di ammortamento: francese o italiano
