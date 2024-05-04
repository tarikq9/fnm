# Regressione lineare
import numpy as np
import matplotlib.pyplot as plt

#TEST
xi=np.array([22,28,35,47,51,56,67,81])
yi=np.array([131,114,121,111,130,145,176,217])

def outputRegressione(input):
    xme = np.mean(xi)
    yme = np.mean(yi)
    devx = xi - xme
    devy = yi - yme
    totsquaredevx = sum((xi - xme)**2)
    totcodev = sum(devx * devy)
    print(len(xi),'osservazioni')
    
    # Stima dei coefficenti
    b1 = round(totcodev / totsquaredevx, 4)
    b0 = round(yme - b1 * xme, 4)

    # Calcolo R^2
    tss = sum((yi - yme)**2)
    yv = b1 * xi + b0
    ess = sum((yv - yme)**2)
    R2 = round(ess / tss, 4)

    # calcola y in funzione di un x a piacere
    output = b1 * input + b0
    print('dato un input di '+str(input)+' ho un output di',output.round(3))

    # Grafico retta OLS
    x = np.linspace(min(xi), max(xi), 100)
    y = b1 * x + b0

    if b0 >= 0:
        plt.plot(x, y, label='y=' + str(b1) + 'x+' + str(b0), color='purple')
    else:
        plt.plot(x, y, label='y=' + str(b1) + 'x' + str(b0), color='purple')

    plt.scatter(xi, yi,color='green')
    plt.scatter(x=input, y=output,color='blue')
    plt.plot([], [], ' ', label='R²=' + str(R2))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(ncol=2,loc='center',bbox_to_anchor=(0.5,1.06))
    plt.grid(linestyle='--', linewidth=0.3)
    plt.show()
outputRegressione(73)
