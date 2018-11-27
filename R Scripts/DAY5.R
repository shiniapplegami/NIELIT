x<-c(6,5,4,5)
pie(x)
movies<-c("Comedy","Action","Romance","Science Fiction")
pie(x,movies,col=c("Red","Purple","Blue","Yellow"),clockwise=TRUE,main="Movie Choices" )
c1<-c("Red","Purple","Blue","Yellow")
legend("topleft",movies,fill= c1,cex=0.5)
-----------------------------------------------------------

x<-c(6,5,4,5)  
movies<-c("Comedy","Action","Romance","Science Fiction")    
barplot(x,xlab="Movie types",ylab="Number of friends",names.arg=movies,col=c("Red","Purple","Blue","Yellow"),main="Movie Choices")
-----------------------------------------------------------

k<-sample(1:20,12,replace = TRUE)
m<-matrix(k,nrow=4,ncol=3)
sales<-c("A","B","C")
barplot(m,xlab="Quarters",ylab="Products",names.arg=sales,main ="Details",col =rainbow(4))
legend("topleft",sales,fill = rainbow(4),cex=0.5)
---------------------------------------------------------------    
  hist(mtcars$mpg,col=rainbow(5),main="MPG")
---------------------------------------------------------------
  
plot.new()
plot.window(xlim =c(0,20),ylim =c(0,20))
axis(1)
axis(2)
x<-sample(1:20,5,replace=TRUE)
y<-sample(1:20,5,replace=TRUE)
points(x,y)
abline(v=20)
abline(h=18)
------------------------------------------------------------

drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)
plot(drugA,type="b")
lines(drugB,type = ("b"))

---------------------------------------------------------------- 
  
airquality  
boxplot(Temp~Month,data = airquality)

----------------------------------------------------------------
  plot(iris$Sepal.Length,iris$Sepal.Width,type = "p",col=rainbow(2))
  
---------------------------------------------------------------------------  
  iris
pairs(~Sepal.Length+
      Sepal.Width+Petal.Length+Petal.Width,data = iris,main="Scatterplot")
--------------------------------------------------------------
  
  