import numpy as np 
import matplotlib.pyplot as plt

#Valori di test
varx='temperatura'
vary='rendimento'
xi = np.array([50,50,50,70,70,70,80,80,80,90,90,90,100,100,100])
yi = np.array([3.3,2.8,2.9,2.3,2.6,2.1,2.5,2.9,2.4,3.0,3.1,2.8,3.3,3.5,3.0])

def regressione(n):
    if n > 9:
        print("Usa un grado minore di 9.")
        return

    coefficenti = np.polyfit(xi, yi, n)
    x = np.linspace(min(xi), max(xi), 100)
    y = np.polyval(coefficenti, x)
    
    # Calcolo R2 
    y_fit = np.polyval(coefficenti, xi)
    R2 = round(1 - sum((yi - y_fit)**2) / sum((yi - np.mean(yi))**2), 4)
    
    # Grafico regressione
    unicode_exponents = {1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
    label_parts = []
    for i, coeff in enumerate(coefficenti.round(4)):
        if (n-i) in unicode_exponents:
            if coeff < 0:
                label_parts.append(f'{coeff}x{unicode_exponents[n-i]}')
            else:
                label_parts.append(f'+ {coeff}x{unicode_exponents[n-i]}')
        elif coeff < 0:
            label_parts.append(str(coeff))
        elif coeff > 0:
            label_parts.append(" + " + str(coeff))
        elif i == 0:
            label_parts.append(str(coeff))
                
    label = 'y = ' + ' '.join(label_parts)
    plt.plot(x, y, label=label, color='purple')
    plt.scatter(xi, yi, color='green')
    plt.plot([], [], ' ', label='R²=' + str(R2))
    plt.xlabel(varx)
    plt.ylabel(vary)
    plt.legend(ncol=2, loc='center', bbox_to_anchor=(0.5, 1.06))
    plt.grid(linestyle='--', linewidth=0.3)
    plt.show()
regressione(2) #inserire il grado della funzione
