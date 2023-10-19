#LEGENDA
#n= rate
#i= tasso di interesse annuo
#k= quanti versamenti annui......inserire 12 se mensili , 6 se bimestrale , 4 trimestrale ecc...
#S= ammontare del debito iniziale

#Ammortamento a quote di capitale costanti
def ammortamentoItaliano(n,i,k,S) :
    import numpy as np
    import pandas as pd 
    from tabulate import tabulate
    
    x=range(1,n+1)
    intervallo=np.array(x)
    iv= (1+i)**(1/k)-1          #iv= il tasso equivalente convertito in base a k
    QuotaCapitale= np.resize(np.round((S/n),2),n)
    DebitoResiduo=np.round(((n-intervallo)/n)*S,2)
    DebitoEstinto=np.round(intervallo*(S/n))
    Interessi= np.round((n-intervallo+1)*(S/n)*iv,2)
    Rata= np.round((QuotaCapitale+Interessi),2)
    
    #Creazione tabella
    
    tabella=pd.DataFrame(zip(intervallo,Rata,QuotaCapitale,Interessi,DebitoResiduo,DebitoEstinto),columns=["N°Rate","Rata","Quote Capitale","Interessi","Debito Residuo","Debito Estinto"])
    riga=pd.DataFrame({"N°Rate":0,"Rata":0,"Quote Capitale":0,"Interessi":0,"Debito Residuo":S,"Debito Estinto":0},index=[0])
    Tabella=pd.concat([riga,tabella.loc[:]]).reset_index(drop=True)
    
    print(tabulate(Tabella,headers="keys",tablefmt="fancy_grid",showindex="never"))
    print("Il totale degli interessi corrisposti sarà di",round(sum(Interessi),2))
ammortamentoItaliano(24,0.03,12,50000)

