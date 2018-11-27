x<-c(1:19, 20:1)
x<-c(4,6,3)
x
x<-c(4,6,3)
rep.int(x,10)

x<-c(4,6,3)
rep(x, length.out=31)

x<-rep(4,10)
y<-rep(6,20)
z<-rep(3,30)
a<-c(x,y,z)

R <- c(2.27, 1.98, 1.69, 1.88, 1.64, 2.14)
H <- c(8.28, 8.04, 9.06, 8.70, 7.58, 8.34)
V=(1/3)*pi*R^2*H
V
round(V,2)
min(V)
max(V)


A<-sample(0:999,250)
B<-which(A>900)
LP<-A[B]
sort(LP)

H<-c(180, 165, 160, 193)
W<-c(87, 58, 65, 100)
h=H/100
BMI=W/h^2
w<-which(BMI>25)
p<-BMI[w]
AVG<-mean(BMI)
M<-sample(0:50,10)
P1<-mean(M)
P2<-median(M)

dry <- c(77, 93, 92, 68, 88, 75, 100)
sum(dry)
length(dry)
mean(dry)
sum(dry)/length(dry) 
sort(dry)
median(dry)
sd(dry)
var(dry)

sd(dry)^2
min(dry)
max(dry)
summary(dry)

               