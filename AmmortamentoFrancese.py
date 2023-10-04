#LEGENDA
#n= numero rate
#i= tasso di interesse annuo
#k= quanti versamenti annui......inserire 12 se mensili , 6 se bimestrali , 4 trimestrali ecc...
#S= ammontare del debito iniziale

#Ammortamento francese, rate costanti 
def ammortamentoFrancese(n,i,k,S) :
    import numpy as np
    import pandas as pd 
    from tabulate import tabulate
    
    x=range(1,n+1)
    intervallo=np.array(x)
    iv= (1+i)**(1/k)-1          #iv= il tasso equivalente convertito in base a k
    Rata= np.resize(np.round(S/((1-(1+iv)**-n)/iv),2),n)
    QuotaCapitale= np.round(((1+iv)**-(n-intervallo+1))*Rata,2)
    Interessi= np.round(((1-(1+iv)**-(n-intervallo+1)))*Rata,2)
    DebitoResiduo=np.round(((1-(1+iv)**(-n+intervallo))/iv)*Rata,2)
    #Creazione tabella
    
    tabella=pd.DataFrame(zip(intervallo,Rata,QuotaCapitale,Interessi,DebitoResiduo),columns=["N°Rate","Rata","Quote Capitale","Interessi","Debito Residuo"])
    riga=pd.DataFrame({"N°Rate":0,"Rata":0,"Quote Capitale":0,"Interessi":0,"Debito Residuo":S},index=[0])
    Tabella=pd.concat([riga,tabella.loc[:]]).reset_index(drop=True)
    
    print(tabulate(Tabella,headers="keys",tablefmt="fancy_grid",showindex="never"))
    print("Il totale degli interessi corrisposti sarà di",round(sum(Interessi),2))
ammortamentoFrancese(48,0.1449,12,2500)
