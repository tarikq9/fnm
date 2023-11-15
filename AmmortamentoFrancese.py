#LEGENDA
# n= Anni o Rate
# v= (v=1 se calcolate in anni) , (v=k se calcolate in rate)
# k= N° versamenti ANNUI
# i= Tasso d'interesse ANNUO
# s= Debito iniziale

 


# Inserire i valori dentro la funzione ammortamentoFrancese riga 60
def ammortamentoFrancese(n,v,k,i,s) :
    #Importo le librerie necessarie 
    import math
    import numpy as np
    import pandas as pd 
    import matplotlib.pyplot as plt
    from tabulate import tabulate
    
    #Rispettivamente : nk= rate del piano , t= iterazione temporale , ik= tasso equivalente 
    nk= math.trunc(n*k/v)                               
    t= np.array(range(1,nk+1))                                        
    ik= (1+i)**(1/k)-1                        
                              
    #Colonne R,QC,I,DR,DE  
    R= np.resize((s/((1-(1+ik)**-nk)/ik)),nk)
    QC= R*((1+ik)**-(nk-t+1))
    I=  R*((1-(1+ik)**-(nk-t+1)))
    DR= R*((1-(1+ik)**(-nk+t))/ik)
    DE= s-DR
    

    #Creazione tabella 
    z=pd.DataFrame(zip(t,R,QC,I,DR,DE),columns=["N°Rate","Rata","Quote Capitale","Interessi","Debito Residuo","Debito Estinto"])
    riga=pd.DataFrame({"N°Rate":0,"Rata":0,"Quote Capitale":0,"Interessi":0,"Debito Residuo":s,"Debito Estinto":0},index=[0])
    T=pd.concat([riga,z.loc[:]]).reset_index(drop=True) 
    pd.set_option('display.precision',2)
    

    #Stampa la tabella
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
ammortamentoFrancese(30,1,1,0.03,100000)