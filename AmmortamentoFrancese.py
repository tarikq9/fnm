#LEGENDA
#n= numero di rate 
#i= tasso di interesse 
#S= ammontare del debito iniziale

#Ammortamento francese, ovvero a rate costanti 
def ammortamentoFrancese(n,i,S) :
    import numpy as np
    import pandas as pd 
    from tabulate import tabulate
    x=range(1,n+1)
    intervallo=np.array(x)
    
    Rata= np.resize(np.round(S/((1-(1+i)**-n)/i),2),n)
    QuotaCapitale= np.round(((1+i)**-(n-intervallo+1))*Rata,2)
    Interessi= np.round(((1-(1+i)**-(n-intervallo+1)))*Rata,2)
    DebitoResiduo=np.round(((1-(1+i)**(-n+intervallo))/i)*Rata,2)
    #Creazione tabella
    Tabella=pd.DataFrame(zip(intervallo,Rata,QuotaCapitale,Interessi,DebitoResiduo),columns=["N°Rate","Rata","Quote Capitale","Interessi","Debito Residuo"])
    

    print(tabulate(Tabella,headers="keys",tablefmt="fancy_grid"))
ammortamentoFrancese(30,0.03,100000)

