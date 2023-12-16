#Legenda 

F = 100               # valore facciale o nominale 
j= 2                  # quanti pagamenti cedolari all'anno
y = 0.03/j            # tasso cedolare convertibile j volte l'anno 
g = 12.5/100          # tassazione sul capital gain
t = 76/180            # frazione di periodo per calcolare i dietimi  
CS = 97.50            # corso secco 
n = 2                 # anni

#Cedolare netto e capitale netto 
ced= F * y * (1-g)
CN= F - (F-CS) * g

#Prezzo Tel quel
Ptq= CS + (t*ced)

#Funzione = 0
def f(ytm):
    return ced * (1-(1+ytm)**-n)/ytm * (1+ytm)**t + CN * (1+ytm)**-(n-t) - Ptq

#Trovo lo ytm, metodo newton raphson  
import scipy.optimize as so 

x0= 0.03
ytm= so.newton(f,x0)                  #j ytm
ytm1= (1+ytm)**j-1                    #annuale 

#Stampo il risultato 
print(f"ytm j volte l'anno = {ytm:.5f}")
print(f"ytm annuale = {ytm1:.5f}")





