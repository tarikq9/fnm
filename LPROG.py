from pulp import *
#inserire LpMaximize per massimizzare o LpMinimize per minimizzare
modello= LpProblem(sense=LpMaximize)  

#Inserisci i coefficenti 
#funzione obiettivo 
o1,o2,o3=[ 1, 1, 0 ]                   

# vincoli         a x   b y   c z  <=> k       1(>=) -1(<=)   
a1,b1,c1,k1, s1 = 0  ,  1 ,   0 ,      2,      1           
a2,b2,c2,k2, s2 = 1  ,  2 ,   0 ,     25,     -1             
a3,b3,c3,k3, s3 =-2  ,  4 ,   0 ,     -8,      1  
a4,b4,c4,k4, s4 =-2  ,  1 ,   0 ,     -5,     -1  


#variabili
x=LpVariable(name='x',lowBound=0)
y=LpVariable(name='y',lowBound=0)
z=LpVariable(name='z',lowBound=0)

#funzione obiettivo e vincoli 
modello += lpSum([o1*x+o2*y+o3*z])
modello +=(s1*(a1*x+b1*y+c1*z)>=k1*s1)
modello +=(s2*(a2*x+b2*y+c2*z)>=k2*s2)
modello +=(s3*(a3*x+b3*y+c3*z)>=k3*s3)
modello +=(s4*(a4*x+b4*y+c4*z)>=k4*s4)

#risolvo il modello
status = modello.solve(solver=PULP_CBC_CMD(msg=False))


#stampo i risultati
print(f"objective: {modello.objective.value()}")
print(f"x: {x.value()}")
print(f"y: {y.value()}")
print(f"z: {z.value()}")

#Importo le librerie per costruire il grafico 
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

#limiti x y 
xl = []
for k, a in zip ([k1, k2,k3,k4], [a1, a2,a3,a4]): 
  try:
    xln = k/a
    
    xl.append (xln)
  except ZeroDivisionError:
    pass

yl = []
for k, b in zip ([k1, k2,k3,k4], [b1, b2,b3,b4]): 
  try:
    yln = k/b
    
    yl.append (yln)
  except ZeroDivisionError:
    pass

h= max(xl+yl)
X=np.linspace(0,h,1000)
np.seterr(divide='ignore',invalid='ignore')

#rette n2
y1=(k1-a1*X)/b1    #nero
y2=(k2-a2*X)/b2    #viola
y3=(k3-a3*X)/b3    #blu
y4=(k4-a4*X)/b4    #verde

#rappresento sul piano
if b1==0 and a1!=0:
    plt.axvline(x=k1/a1,color='orange',label='1°vincolo')
else:
    ax.plot(X,y1,color='orange',label='1°vincolo')

if b2==0 and a2!=0:
    plt.axvline(x=k2/a2,color='blue',label='2°vincolo')
else:
    ax.plot(X,y2,color='blue',label='2°vincolo')

if b3==0 and a3!=0:
    plt.axvline(x=k3/a3,color='green',label='3°vincolo')
else:
    ax.plot(X,y3,color='green',label='3°vincolo')

if b4==0 and a4!=0:
    plt.axvline(x=k4/a4,color='purple',label='4°vincolo')
else:
    ax.plot(X,y4,color='purple',label='4°vincolo')

plt.plot(x.value(), y.value(),'ro',label='ottimo')
#disegno la regione ammissibile
xx, yy = np.meshgrid(X, X)

cond1 = (s1*(a1*xx + b1*yy) >= k1*s1)
cond2 = (s2*(a2*xx + b2*yy) >= k2*s2)
cond3 = (s3*(a3*xx + b3*yy) >= k3*s3)
cond4 = (s4*(a4*xx + b4*yy) >= k4*s4)

RegioneAmmissibile = cond1 & cond2 & cond3 & cond4
plt.imshow(RegioneAmmissibile, extent=[0, h, 0, h], origin='lower', cmap='PuBu', alpha=0.2, zorder=0, aspect='auto')

plt.xlim(0,max(xl))
plt.ylim(0,max(yl))
plt.grid(linestyle='--',linewidth=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grafico vincoli e punto di ottimo xy')
plt.legend()
if c1==0 and c2==0 and c3==0 and c4==0:
   plt.show()