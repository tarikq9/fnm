#Comandi base di R 

#Assegna un valore ad una variabile (esempio: a)
a<-1
a

#Modifica un valore già assegnato ad a
a<-4
a

#Crea un vettore di nome italia che contiene elementi numerici
italia<- c(1,2,3,4)
italia


#Estrai un valore dal vettore
italia[3]

#Modifica valore dentro il vettore
italia[3]<-8
italia[3]


#Calcoli con R
7+6
9^2
italia*3
italia*italia

#Comando stampa simil Phyton
print("Europa")
print(italia)

#Funzione concatenate con incolla(paste)
testo<- "è un paese europeo"
paste("L'italia",testo)

#Assena lo stesso valore a diverse variabili
var1<-var2<-var3<-"africa"
var1
var2
var3

#Chiedere ad R se è il tipo di variabile corretto
is.character(testo)
is.numeric(italia)

#Uso del comando class per chiedere che tipo di variabile è
N<-60L
class(N)

#Assegna un valore logico ad N e poi controlla
N<- FALSE
class(N)

#Conversione del tipo di variabile con comando as.
N<-60L
as.numeric(N)

#Escape character per accettare gli errori
Paris="Parigi è \"in mezzo\",alla francia"
Paris

#Logica Vero e falso
9<10
10>100

#Logica con if else
a<-10
b<-90

if(b>a) {
  print("l'africa è più grande dell'europa")
} else {
  print("l'europa è più grande dell'africa")
}

#LOOP con while: stampa una serie crescente, che non supera il 6
i<-1
while(i<6){
  print(i)
  i<-i+1
}

#Loop con comando for
tentativo<-c(1,2,3,4,5,6)
for(x in tentativo) {
  print(x)
}

#comando break per interrompere un loop con for 
for(x in tentativo) {
  if(x==4) { break}
  print(x)
}

#Creare una funzione
funzione1<-function(){
  print("come va")
  }
funzione1()

#Funzione più elaborata con paste
funzione2<-function(nome){
  paste(nome,"bianchi")
  }
funzione2("marco")
funzione2("giovanni")
funzione2("silvio")


#funzione con argomento x 
funzione3<-function(n){
  return(5*n)
  }
funzione3(2)
funzione3(5)
funzione3(20)


#Assegna valore globale 

message("un valore creato all'interno di una funzione può essere
esteso a tutto l'ambiente con il comando < < - ")

#CONCLUSIONE DEL TUTORIAL


#INIZIO STRUTTURA DEI DATI 

#creazione vettore di nome vettore1 con numeri da 1 a 9
vettore1<- c(1:9)
vettore1

#Controlla quanti caratteri ha vettore1
length(vettore1)

#Metti in ordine i caratteri di un nuovo vettore chiamato vettore2
vettore2<-c(1,4,6,0,5,19,12)
sort(vettore2)
vettore2

#Estrai il primo e il settimo elemento di : vettore1
vettore1[c(1,7)]

#Vettore con la funzione seq , creiamo vettore3
message("sequenza da 30 fino a 150, facendo salti di 15")

vettore3<-seq(from=30, to=150,by=15)
vettore3

#Crea una lista di nome lista1
lista1<-list("cane","gatto","topo","cavallo")
lista1

#Controlla se un elemento esiste nella lista1
"topo" %in% lista1
"maiale" %in% lista1

#Aggiungere un elemento alla lista 
append(lista1,"leone")

#Estrai dal primo al terzo elemento da lista1
lista1[c(1:3)]


#Costruisci matrice con il comando matrix riempita per righe
matrice<- matrix(data=vettore1,nrow=3,ncol=3,byrow=T)
matrice

#estrai dati dalla matrice
matrice[,3]       #tutta la terza colonna
matrice[1,3]      #l'elemento che sta sulla prima riga e terza colonna
matrice[3,]       #tutta la terza riga
matrice[c(1,2),]  #le prime due righe

#Crea nuova matrice con cbind e aggiungi colonna
nuovamatrice<-cbind(matrice,c(11,12,13))
nuovamatrice

#Aggiungi riga invece che colonna con rbind
nuovamatrice2<-rbind(matrice,c(11,12,13))
nuovamatrice2

#Rimuovi colonne o righe dalla matrice
nuovamatrice2[-c(2),-c(4)]

#Conoscere il numero di righe e colonne
dim(nuovamatrice2)

#Mettere insieme due matrici
Doppiamatrice<- rbind(matrice,nuovamatrice2)
Doppiamatrice

#Creazione array
array1<- c(1:24)
array1

#l'array ha più di una dimensione, vediamo come
modarray<- array(array1,dim=c(4,3,2))
modarray

#Estrai elemento dal nuovo array
modarray[1,3,2]

#Controlla se il valore esiste nel array
2 %in% modarray

#ammontare di righe e colonne
dim(modarray)

#Loop in modarray
for(x in modarray){
  print(x)
}

#Costruisco un dataframe
dataframe1<- data.frame(allenamento=c("forza","resistenza","corsa"),
                        battito=c(100,120,150), velocità=c(10,20,30))
dataframe1

#sommario del dataframe
summary(dataframe1)

#estrai elementi dal dataframe
dataframe1$allenamento
dataframe1[[2]]

#aggiungi una riga con rbind
dataframe2<- rbind(dataframe1,c("Technique", 7/10, 9/10))
dataframe2

#aggiungi colonna con cbind
dataframe3<-cbind(dataframe1, disciplina=c(3/10,6/10,8/10))
dataframe3

#numero di righe e colonne di un dataframe
dim(dataframe1)

#crea un factor
generi.musicali<-factor(c("rock","rap","jazz","hip hop"))
print(generi.musicali)

#levels per avere solo gli elementi dentro
levels(generi.musicali)

#Cambia elemento interno di un factor
generi.musicali[4]<-"opera"
#da errore poichè va aggiunto l'elemento su factor sotto forma di levels

#PARTE GRAFICA, PLOT!
#creazione grafico individuando un punto
plot(1,7)

#grafico con due punti
plot(c(1,10),c(3,15))

#altro plot
x<-c(1,2,3,4,5)
y<-c(5,10,15,20,25)
plot(x,y)

#disegnare una retta
plot(10:100, type="l",col="blue")

#modifica il grafico
plot(1:10, main="Grafico1", xlab="Asse X", ylab="Asse y"
     ,col="purple",cex=2,pch=8)

#Disegnare due rette nello stesso grafico
line1<-c(2,4,6,8,10,12)
line2<-c(3,6,9,12,15,18)
plot(line1,type="l",col="green")
lines(line2,type="l",col="blue")


#Grafici a barre
animali<-c("scimmia","lucciole","cani","testuggini")
vita.media <- c(40,10,25,120)
barplot(vita.media,names.arg=animali,col="purple")

#Barplot orizzontali
barplot(vita.media,names.arg=animali,col="purple",horiz=TRUE)

#R STATISTIC
#carichiamo un elenco di dati già presente
mtcars

#informazioni sul dataset
?mtcars

#sommario dataset
cars<-mtcars
summary(cars)

#restituisci nomi righe della prima colonna
rownames(cars)

#restituisci i valori di questa variabile
cars$cyl

#massimi e minimi di una variabile di un dataset
max(cars$hp)
min(cars$hp)

#Capire a quale osservazione appartiene il valore massimo o minimo 
which.max(cars$hp)
which.min(cars$hp)

#Estrarre il nome dell'osservazione 
rownames(cars)[which.max(cars$hp)]
rownames(cars)[which.min(cars$hp)]

#media moda mediana
carsW <-cars$wt[1:32]
sort(carsW)
carsW

#Calcoliamo ora media mediana moda*
mean(carsW)
median(carsW)
names(sort(-table(cars$wt)))[1]

#Calcoliamo un percentile di 75%
quantile(carsW,c(0.75))

#Calcoliamo un quartile
quantile(carsW)

