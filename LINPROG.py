from pulp import *
#inserire LpMaximize per massimizzare o LpMinimize per minimizzare
modello= LpProblem(sense=LpMaximize)  

#Inserisci i coefficenti 
#funzione obiettivo 
z1,z2=[ -3 , 12 ]                   

# vincoli       x   y  <=> c    1(>=) -1(<=)   
a1,b1,c1, s1 =[ 7 ,-1,   3    ,    - 1  ]         
a2,b2,c2, s2 =[ -3 , 6 ,  10   ,    -1  ]           
a3,b3,c3, s3 =[ 3 , 4 ,   9   ,     -1  ]
a4,b4,c4, s4 =[ 3 , 3 ,   3   ,     1  ]


#variabili
x=LpVariable(name='x',lowBound=0)
y=LpVariable(name='y',lowBound=0)


#funzione obiettivo e vincoli 
modello += lpSum([z1*x+z2*y])
modello +=(s1*(a1*x+b1*y)>=c1*s1)
modello +=(s2*(a2*x+b2*y)>=c2*s2)
modello +=(s3*(a3*x+b3*y)>=c3*s3)
modello +=(s4*(a4*x+b4*y)>=c4*s4)


#risolvo il modello
status = modello.solve(solver=PULP_CBC_CMD(msg=False))


#stampo i risultati
print(f"objective: {modello.objective.value()}")
print(f"x: {x.value()}")
print(f"y: {y.value()}")



#Importo le librerie per costruire il grafico 
import numpy as np
import matplotlib.pyplot as plt

#limiti x y del grafico
xl = []
for c, a in zip ([c1, c2,c3,c4], [a1, a2,a3,a4]): 
  try:
    xln = c/a
    
    xl.append (xln)
  except ZeroDivisionError:
    pass

yl = []
for c, b in zip ([c1, c2,c3,c4], [b1, b2,b3,b4]): 
  try:
    yln = c/b
    
    yl.append (yln)
  except ZeroDivisionError:
    pass

h = max (xl+yl)+1

xr=np.linspace(0,h,300)
np.seterr(divide='ignore',invalid='ignore')   #ignora le divisioni per zero 

#disegno le rette 
y1=(c1-a1*xr)/b1
y2=(c2-a2*xr)/b2
y3=(c3-a3*xr)/b3
y4=(c4-a4*xr)/b4

fig, ax = plt.subplots()

if a1==0 and b1==0 and c1==0:
   label=None
else:
   label='vincolo 1'
if label is None:
   ax.plot(xr,y1,color='purple')
else:
   ax.plot(xr,y1,color='purple',label=label)


if a2==0 and b2==0 and c2==0:
   label=None
if label is None:
   ax.plot(xr,y2,color='darkgreen')
else:
   ax.plot(xr,y2,color='darkgreen',label='vincolo 2')


if a3==0 and b3==0 and c3==0:
   label=None
if label is None:
   ax.plot(xr,y3,color='darkblue')
else:
   ax.plot(xr,y3,color='darkblue',label='vincolo 3')


if a4==0 and b4==0 and c4==0:
   label=None
if label is None:
   ax.plot(xr,y4,color='black')
else:
   ax.plot(xr,y4,color='black',label='vincolo 4')


if b1==0:
    plt.axvline(x=c1,color='purple')
if b2==0:
    plt.axvline(x=c2,color='darkgreen')
if b3==0:
    plt.axvline(x=c3,color='darkblue')
if b4==0:
    plt.axvline(x=c4,color='black')

plt.plot(x.value(), y.value(),'ro',label='ottimo')

#disegno la regione ammissibile
xx, yy = np.meshgrid(xr, xr)
cond1 = (s1*(a1*xx + b1*yy) >= c1*s1)
cond2 = (s2*(a2*xx + b2*yy) >= c2*s2)
cond3 = (s3*(a3*xx + b3*yy) >= c3*s3)
cond4 = (s4*(a4*xx + b4*yy) >= c4*s4)

RegioneAmmissibile = cond1 & cond2 & cond3 & cond4
plt.imshow(RegioneAmmissibile, extent=[0, h, 0, h], origin='lower', cmap='PuBu', alpha=0.15, zorder=0, aspect='auto')

#stampo il grafico 
plt.grid(linestyle='--',linewidth=0.5)
plt.legend(ncol=5,loc='center',bbox_to_anchor=(0.5,1.06))
plt.xlim(0)
plt.ylim(0)
plt.show()


