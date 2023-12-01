M= 50000               # montante
n= 5                   # anni o rate 
i= 0.02                # tasso d'interesse ANNUO
k= 12                  # n° versamenti o prelievi annui 


#Rata costante che costituisce un montante da depositare
def V(v) :
  nk= n*k/v                          
  ik= (1+i)**(1/k)-1               
  S= ((1+ik)**nk-1)/ik
  Rata= round(M/S,2)
  print("il versamento costante ha un valore di ",Rata )
V(1)  #v=1 se in anni , v=k se in rate 

#Rata costante che consuma un capitale depositato
def P(v) :
  nk= n*k/v
  iv= (1+i)**(1/k)-1
  A= (1-(1+iv)**-nk)/iv
  Rata= round(M/A,2)
  print("Il prelievo costante ha un valore di ",Rata)
P(1)  # v=1 se in anni , v=k se in rate 


#Calcolo REA e TIR con npv e irr

import numpy_financial as npf

#Calcolo REA 
tasso,flussi= 0.03,[-100,100,125,150,175]
print(npf.npv(tasso,flussi).round(2))

#Calcolo TIR 
TIR= round(npf.irr([-500,500,30,3,10]),2)
print(TIR)