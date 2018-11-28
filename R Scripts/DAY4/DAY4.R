
A<-data.frame (sname=c("Alex","Lilly","Mark"),Age=c(25,31,23),Height=c(177,163,190),Weight=c(57,69,83),Sex=c("F","F","M"))
A
------------------------------------------
B<-data.frame (Working=c("Yes","No","No"))

D<-cbind(A, B)
lapply(A, class)

mean(A[,3])

BMI<- A[,4]/(A[,3]/100)**2
E<-cbind(D,BMI)

healthy<- ifelse(BMI<25, "YES", "NO")
F<-cbind(E,healthy)
F
-----------------------------------------
m<-read.table (file.choose())
r1<-m
r1

r2<-read.csv (file.choose())
-----------------------------------------
r<-c("r1","r2")
c<-c("c1","c2","c3")
m<-c("m1","m2","m3")
A<-array(1:20,dim=c(2,3,3),list(r,c,m))
A
----------------------------------------
mtcars  
 
mix<-data.frame(mp=mtcars$mpg,cyl=mtcars$cyl,hp=mtcars$hp)
mix
-----------------------------------------
t1<-head(mtcars,5)
t1
t2<-tail(mtcars,5)
t2
t3<-rbind(t1,t2)
t3
----------------------------------------
add<-function(a,b=1)
{
  x=a+b
  print(x)
}
  add(2)
  
  add<-function(a,b)
  {
    x=a+b
    print(x)
  }
  add(b=2,a=3)
-----------------------------------------
    print(getwd())
  