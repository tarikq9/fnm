#Inserisci coefficenti funzione obiettivo
z1,z2=[ 20 , 10 ]            

#inserire i coefficenti dei vincoli
#nell'ultimo termine tenere 1 se >, inserisci -1 se <

#               x   y   c     >=/<=
a1,b1,c1, s1 =[ 1 , 2 , 40,  -1   ]         
a2,b2,c2, s2 =[ 3 , 1 , 30,   1   ]           
a3,b3,c3, s3 =[ 4 , 3 , 60,   1   ]
a4,b4,c4, s4 =[ 0 , 0 , 0 ,   1   ]



#Importo librerie 
import numpy as np
from pulp import LpMaximize, LpProblem, LpStatus,lpSum,LpVariable,PULP_CBC_CMD as pcc,LpMinimize
import matplotlib.pyplot as plt

#Definisci il tipo di problema
modello= LpProblem(sense=LpMaximize)

#Variabili
x=LpVariable(name='x',lowBound=0)
y=LpVariable(name='y',lowBound=0)


#funzione obiettivo e vincoli 
modello += lpSum([z1*x+z2*y])
modello +=(s1*(a1*x+b1*y)>=c1*s1)
modello +=(s2*(a2*x+b2*y)>=c2*s2)
modello +=(s3*(a3*x+b3*y)>=c3*s3)
modello +=(s4*(a4*x+b4*y)>=c4*s4)

#risolvo il modello
status = modello.solve(solver=pcc(msg=False))

#Stampo i risultati
print(f"objective: {modello.objective.value()}","è il profitto massimo")
print(f"x: {x.value()}")
print(f"y: {y.value()}")

#Grafico con matplotlib
xl = []
for c, a in zip ([c1, c2,c3,c4], [a1, a2,a3,a4]): 
  try:
    xln = c/a
    
    xl.append (xln)
  except ZeroDivisionError:
    pass

h = max (xl)

xr=np.linspace(0,h,1000)
np.seterr(divide='ignore',invalid='ignore')

y1=(c1-a1*xr)/b1
y2=(c2-a2*xr)/b2
y3=(c3-a3*xr)/b3
y4=(c4-a4*xr)/b4

fig, ax = plt.subplots()
fig.set_size_inches(7, 5)

if a1==0 and b1==0 and c1==0:
   label=None
else:
   label='vincolo 1'
if label is None:
   ax.plot(xr,y1,color='brown')
else:
   ax.plot(xr,y1,color='brown',label=label)


if a2==0 and b2==0 and c2==0:
   label=None
if label is None:
   ax.plot(xr,y2,color='darkgreen')
else:
   ax.plot(xr,y2,color='darkgreen',label='vincolo 2')


if a3==0 and b3==0 and c3==0:
   label=None
if label is None:
   ax.plot(xr,y3,color='blue')
else:
   ax.plot(xr,y3,color='blue',label='vincolo 3')


if a4==0 and b4==0 and c4==0:
   label=None
if label is None:
   ax.plot(xr,y4,color='orange')
else:
   ax.plot(xr,y4,color='orange',label='vincolo 4')


if b1==0:
    plt.axvline(x=c1,color='purple')
if b2==0:
    plt.axvline(x=c2,color='brown')
if b3==0:
    plt.axvline(x=c3,color='blue')
if b4==0:
    plt.axvline(x=c4,color='orange')

ax.scatter(x.value(), y.value(), s=30, color='red',label='ottimo')

#Condizioni per la regione ammissibile
xx, yy = np.meshgrid(xr, xr)
cond1 = (s1*(a1*xx + b1*yy) >= c1*s1)
cond2 = (s2*(a2*xx + b2*yy) >= c2*s2)
cond3 = (s3*(a3*xx + b3*yy) >= c3*s3)
cond4 = (s4*(a4*xx + b4*yy) >= c4*s4)

RegioneAmmissibile = cond1 & cond2 & cond3 & cond4
ax.imshow(~RegioneAmmissibile, extent=(xr.min(), xr.max(), xr.min(), xr.max()), origin='lower', cmap='ocean',alpha=0.1)


plt.grid(linestyle='--',linewidth=0.5)
plt.legend(ncol=5,loc='center',bbox_to_anchor=(0.5,1.06))
ax.set_aspect(0.75)
plt.show()


