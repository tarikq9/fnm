#LEGENDA, inserire i valori in basso

n=30                # Anni o Rate
k=1                 # N° versamenti ANNUI
i=0.03              # Tasso d'interesse ANNUO 
s=100000            # Debito iniziale

 

def ammortamentoFrancese(v) :
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
    R= np.full(nk,s/((1-(1+ik)**-nk)/ik))
    QC= R*((1+ik)**-(nk-t+1))
    I=  R*((1-(1+ik)**-(nk-t+1)))
    DR= R*((1-(1+ik)**(-nk+t))/ik)
    DE= s-DR
    

    #Creazione tabella 
    z=pd.DataFrame(zip(t,R,QC,I,DR,DE),
    columns=["N°Rate","Rata","Quote Capitale","Interessi","Debito Residuo","Debito Estinto"])
    riga=pd.DataFrame({"N°Rate":0,"Rata":0,"Quote Capitale":0,"Interessi":0,"Debito Residuo":s,"Debito Estinto":0},index=[0])
    T=pd.concat([riga,z]).reset_index(drop=True) 
    

    #Stampa tabella e risultati 
    print(tabulate(T,headers="keys",tablefmt="fancy_grid",floatfmt=[".0f", ".2f", ".2f", ".2f", ".2f", ".2f"],showindex="never"))
    print("Totale Interessi:",round(sum(I),2))
    print("Importo totale da restituire: ",round(s+sum(I),2))
    print("Incidenza interessi :",round(100*(sum(I))/(s),2),'%')


    #Stampa il grafico : andamento e incidenza interessi rispetto al capitale prestato
    T["Cumsum"] = T["Interessi"].cumsum()
    T["Cumsum"].plot(x="N°Rate",y="Interessi",label="Interessi cumulati")
    
    plt.hlines(y=s+(round(sum(I),2)),xmin=0,xmax=nk,color="purple",linestyles="-",label="Totale da restituire")
    plt.hlines(y=s,xmin=0,xmax=nk,color="green",linestyles="-",label="Debito iniziale")
    plt.vlines(x=nk,ymin=0,ymax=round(sum(I),2),color="red",linestyle="--",label="Incidenza Interessi")
   
    plt.xlabel("RATE")
    plt.ylabel('Euro')
    plt.grid(linestyle='--',linewidth=0.5)
    plt.legend(ncol=4,loc='center',bbox_to_anchor=(0.5,1.06))
    plt.show()
ammortamentoFrancese(1) #inserire 1 se calcolate anni, inserire il valore di k, se in le rate