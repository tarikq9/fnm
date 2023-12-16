#Calcolo VAN e TIR con npv e irr

import numpy_financial as npf

#Calcolo VAN 
tasso,flussi= 0.03,[-100,100,125,150,175]
print(npf.npv(tasso,flussi).round(2))

#Calcolo TIR 
TIR= round(npf.irr([-500,500,30,3,10]),2)
print(TIR)