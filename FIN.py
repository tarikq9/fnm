M= 50000       # montante
n= 5           # anni o rate 
i= 0.02        # tasso d'interesse ANNUO
k= 12          # n° versamenti o prelievi annui 
v=1            # v=1 calcolo in anni , v=k in rate

#versamenti per costituire o prelevamenti per consumare un capitale
def F(tipo) :
  nk= n*k/v                          
  ik= (1+i)**(1/k)-1 
  if tipo=='versamento':              
    X= ((1+ik)**nk-1)/ik
    Rata= round(M/X,2)
    print("Il versamento costante ha un valore di ",Rata,'euro')
  elif tipo=='prelievo':
    X= (1-(1+ik)**-nk)/ik
    Rata= round(M/X,2)
    print("Il prelievo costante ha un valore di ",Rata,'euro')
F('prelievo')  #specificare se prelievo o versamento

