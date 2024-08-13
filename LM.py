# Regressione lineare semplice
import numpy as np
import matplotlib.pyplot as plt
import math
# inserire i dati nelle variabili
#TEST
xi=np.array([0.9,1.8,2.4,3.5,3.9,4.4,5.1,5.6,6.3])
yi=np.array([1.4,2.6,1.0,3.7,5.5,3.2,3.0,4.9,6.3])

def outputRegressione(input):
    n= len(xi)
    xme = np.mean(xi)
    yme = np.mean(yi)
    devx = xi - xme
    devy = yi - yme
    totsquaredevx = sum((xi - xme)**2)
    totcodev = sum(devx * devy)
    
    # Stima dei coefficenti
    b1 = round(totcodev / totsquaredevx, 4)
    b0 = round(yme - b1 * xme, 4)

    # Calcolo R^2
    tss = sum((yi - yme)**2)
    yv = b1 * xi + b0
    ess = sum((yv - yme)**2)
    R2 = round(ess / tss, 4)
    R2adj= round(1- (((1-R2)*(n-1))/(n-1-1)),4)
    
    # calcola y in funzione di un x a piacere
    output = b1 * input + b0
    print('dato un input di '+str(input)+' ho un output di',output.round(3))

    #Residui
    residui= yi-(b1*xi+b0)
    print('residui =',residui)

    #Errore standard b1
    SEb1= round(math.sqrt((tss-b1*totcodev) / ((n-2)*totsquaredevx)),4)
    

    #T osservato
    T_test = round((b1-0)/SEb1,4)
    
    #ecc... incompleto, mancano  p-value + test d'ipotesi sui coefficenti 
    
    # Grafico retta OLS
    fig, ax= plt.subplots()
    x = np.linspace(min(xi), max(xi), 100)
    y = b1 * x + b0
    
    plt.plot(x,y,color='purple')

    if b0>=0: labelz= 'y=' + str(b1) + 'x+' + str(b0)
    else: labelz= 'y=' + str(b1) + 'x' + str(b0)

    plt.scatter(xi, yi,color='green')
    plt.scatter(x=input, y=output,color='blue')
    plt.plot([], [], ' ', label='R² =' + str(R2))
    plt.plot([], [], ' ', label='R²adjusted =' + str(R2adj))
    plt.plot([], [], ' ', label='SE(b1) =' + str(SEb1))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title(labelz)
    plt.grid(linestyle='--', linewidth=0.3)
    ax.set_facecolor('floralwhite')
    plt.show()
outputRegressione(3.2)
