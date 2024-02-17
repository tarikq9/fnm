#Script per l'esame di eipe commercio estero A-la
#Sono stati usati valori a caso nella funzione per testare gli script
#Evidenzia ed avvia lo script che ti interessa con ctrl invio


#DA DECIMALE A BINARIO
decbin<-function(n) {
  if(n>1) {decbin(as.integer(n/2))}
  cat(n%%2)
}
decbin(15)

#DA BINARIO A DECIMALE 
bindec<-function(binario) {
  dec=0
  n=nchar(binario)
  for(i in 1:n) {
    coefficente<-as.numeric(substr(binario,i,i))
    if(coefficente!=0 & coefficente!=1) stop("error")
    dec=dec+coefficente*2^(n-i)
    
  }
  return(dec)
}
bindec(1111)


#BREAKEVEN POINT
breakpoint<-function(cf,cvu,ru) {
  if(cf<0|cvu<0|ru<0) stop("inserire positivi")
  margine<- ru-cvu
  qta<- cf/margine
  message("la qta ricercata è ",qta," 
 il ricavo totale ammonta a ",qta*ru)
}
breakpoint(4000,30,40)


#CAPITALIZZAZIONE SEMPLICE
Montante<-function(c,r,t) {
  if(c<0|r<0|t<0) stop("errore")
  ct<-c+(c*r*t)
  return(ct)
}
Montante(3000,0.06,4)


#CAPITALIZZAZIONE COMPOSTA 
montanteC<-function(c,r,t) {
  if(c<0|r<0|t<0) stop("errore")
  ct=c*(1+r)^t
  message("capitalizzando ",c," al tasso ",r," per ",t," anni "," ottengo
  un montante di ",ct)
  
}
montanteC(3000,0.06,4)


#RETTA PASSANTE PER DUE PUNTI
rettapassante<-function(yb,ya,xb,xa) {
  m=(yb-ya)/(xb-xa)
  q=ya-m*xa
  
  y<-paste("y =",m,"x +",q)
  message("l'equazione della retta passante per i due punti è ",y)
}
rettapassante(3,6,3,0)


#FUNZIONE CON LOGARITMO
funclog <- function(x){
  if(!is.numeric(x))
    stop("Errore input")
  
  y=ifelse(abs(x)>=sqrt(3),
           sqrt(x^2-3)/log(x^2-x),NA)
  return(y)
}
funclog(c(-4,3,3,5))

#EQUAZIONE DI SECONDO GRADO
quad2<-function(a,b,c) {
  if(a==0|!is.numeric(b) | !is.numeric(c)) stop("errore")
  delta<- b^2-4*a*c
  if(delta<0) stop("non ammette soluzioni reali")
  x1<- (-b+sqrt(delta))/(2*a)
  x2<- (-b-sqrt(delta))/(2*a)
  return(list(x1,x2))
}
quad2(2,8,6)

#TRIANGOLO ISOSCELE
triso<-function(lato,base) {
  if(!is.numeric(lato)|!is.numeric(base)|lato<(base/2)) stop("errore")
  altezza<- sqrt(lato^2 - (base/2)^2)
  area<- (base*altezza)/2
  perimetro<- lato*2+base
  return(list(area,perimetro))
  
}
triso(20,8)

#CERCHIO
cerchio<-function(r) {
  if(r<0|!is.numeric(r)) stop("errore")
  area<-round(r^2*pi)
  perimetro<-round(2*r*pi)
  return(list(perimetro,area))
}
cerchio(9)

#SISTEMA DI EQUAZIONI LINEARI
A<-matrix(c(3,2,-4,-5,5,1,0,7,-2),ncol=3,nrow=3,byrow=T)
B<-c(-5,8,8)
solve(A,B)


#PI GRECO CON RIEEMAN

rieman<-function(n) {
  if(n<1|n%%1>0) stop("inserire intero positivo")
  pgreco<-(90*sum(1/(1:n)^4))^(1/4)
  return(pgreco)
}
rieman(500)

#VEDERE SE UN NUMERO E' PARI O DISPARI
paridispari<-function() {
  n=as.numeric(readline("inserire valore "))
  y=ifelse(n%%2==0,
           tipo<-"pari",
           tipo<-"dispari")
  message("il numero è ",n," ed è ",tipo)
  return(y)
  
}
paridispari()
89

#VALORE ATTUALE
va<-function(m,s,t) {
  if(m<0|s<0|t<0) stop("inserire positivi")
  c<- m*(1+s)^(-t)
  return(c)
}
va(7000,0.05,3)

#MEDIA PESATA
mediaponderata<-function(voti,cfu) {
  if(length(voti)!= length(cfu)) stop("vettori non compatibili")
  if(any(voti>30)|any(cfu>12)) stop("valori superiori ai consentiti ")
  media<-weighted.mean(voti,cfu)
  message("la media ponderata degli esami è di ",media)
  return(media)
}
mediaponderata(c(23,28,30,24),c(6,6,12,12))

