a<-c(2, 3, 5, 7, 8)
w<-c(14, 20, 32, 42, 44)
lm(w~a)


rel<-lm(w~a)
k<-data.frame(a=6)
predict(rel,k)


plot.new()
plot.window(xlim = c(0,10), ylim=(0,50))
abline(rel)
plot(a,w)
#-----------------------------------------------------------------------------------

x<-c(8,7,6,4,2,1)
y<-c(15,19,25,23,34,40)
cor(x,y)

rel<-lm(x~y)

rell<-lm(y~x)
k<-data.frame(x=5)
predict(rell,k)
#--------------------------------------------------------------------------------

m<-c(6,4,8,5,3.5)
c<-c(6.5,4.5,7,5,4)
lm(c~m)
relation<-lm(c~m)
l<-data.frame(m=7.5)
predict(relation,l)
#--------------------------------------------------------------------------------

X<-c(186, 189, 190, 192, 193, 193, 198, 201, 203, 205)
Y<-c(85, 85, 86, 90, 87, 91, 93, 103, 100, 101)
lm(Y~X)
cor(X,Y)
rel2<-lm(Y~X)
p<-data.frame(X=208)
predict(rel2,p)
#-------------------------------------------------------------------------------

X<-c(80, 79, 83, 84, 78, 60, 82, 85, 79, 84, 80, 62)
Y<-c(300, 302, 315, 330, 300, 250, 300, 340, 315, 330, 310, 240)
lm(Y~X)
cor(X,Y)
#-------------------------------------------------------------------------------

x<-c(6, 7, 8, 9, 10)
y<-c(4, 3, 3, 2, 1)
cor(x,y)
rela<-lm(y~x)
o<-data.frame(x=8)
predict(rela,o)
#------------------------------------------------------------------------------

X<-c(25, 42, 33, 54, 29, 36)
Y<-c(42, 72, 50, 90, 45, 48)
cor(X,Y)
rel<-lm(Y~X)
t<-data.frame(X=47)
predict(rel,t)